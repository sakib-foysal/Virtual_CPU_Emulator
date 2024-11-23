class ALU:
    def execute(self, operand1, operand2, operation):
        if operation == "ADD":
            return operand1 + operand2
        elif operation == "SUB":
            return operand1 - operand2
        elif operation == "AND":
            return operand1 & operand2
        elif operation == "OR":
            return operand1 | operand2
        else:
            raise ValueError("Unsupported operation")

class Registers:
    def __init__(self, size=8):
        self.registers = [0] * size  # Initialize all registers to 0

    def read(self, index):
        return self.registers[index]

    def write(self, index, value):
        self.registers[index] = value

class ProgramCounter:
    def __init__(self):
        self.value = 0  # Start at address 0

    def increment(self):
        self.value += 1

    def set(self, address):
        self.value = address


class InstructionRegister:
    def __init__(self):
        self.instruction = None

    def load(self, instruction):
        self.instruction = instruction


# Example of integration
alu = ALU()
registers = Registers()
pc = ProgramCounter()
ir = InstructionRegister()

# Simulate fetching an instruction
instructions = ["LOAD R1, 5", "ADD R1, 3", "STORE R1, R2"]  # Example instructions

while pc.value < len(instructions):
    # Fetch
    current_instruction = instructions[pc.value]
    ir.load(current_instruction)

    # Decode and execute
    print(f"Executing: {ir.instruction}")
    tokens = ir.instruction.split()

    if tokens[0] == "LOAD":
        # LOAD R1, 5
        reg_index = int(tokens[1][1])  # Extract register index (R1 -> 1)
        value = int(tokens[2])
        registers.write(reg_index, value)
        print(f"Loaded {value} into R{reg_index}")

    elif tokens[0] == "ADD":
        # ADD R1, 3
        reg_index = int(tokens[1][1])  # Extract register index (R1 -> 1)
        operand1 = registers.read(reg_index)
        operand2 = int(tokens[2])
        result = alu.execute(operand1, operand2, "ADD")
        registers.write(reg_index, result)
        print(f"Added {operand1} and {operand2}, stored {result} in R{reg_index}")

    elif tokens[0] == "STORE":
        # STORE R1, R2
        reg_index_src = int(tokens[1][1])  # Source register index (R1 -> 1)
        reg_index_dest = int(tokens[2][1])  # Destination register index (R2 -> 2)
        value = registers.read(reg_index_src)
        registers.write(reg_index_dest, value)
        print(f"Stored value {value} from R{reg_index_src} into R{reg_index_dest}")

    else:
        print(f"Unknown instruction: {tokens[0]}")

    # Increment program counter
    pc.increment()

    # Print state of registers after every instruction
    print("Register State:", registers.registers)

# Final state of registers
print("\nFinal Register State:")
for i, reg in enumerate(registers.registers):
    print(f"R{i}: {reg}")

