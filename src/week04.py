# Instruction memory
# Load value 10 into register R1  Add the value of R2 to R1# Store the value of R1 at memory address 20
memory = [ "LOAD R1, 10", "ADD R1, R2", "STORE R1, 20" ] 

# Registers and program counter initialization
registers = {"R1": 0, "R2": 5}  # Initialize registers
pc = 0  # Program Counter starts at 0

# Function to decode an instruction
def decode(instruction):
    parts = instruction.split()  # Split into operation and operands
    opcode = parts[0]  # The operation (e.g., LOAD, ADD, STORE)
    operands = parts[1:]  # The arguments (e.g., R1, 10)
    return opcode, operands

# Function to execute an instruction
def execute(opcode, operands):
    if opcode == "LOAD":
        reg, value = operands[0], int(operands[1])  # Extract register and value
        registers[reg] = value  # Load the value into the register
    elif opcode == "ADD":
        reg1, reg2 = operands[0], operands[1]  # Extract the two registers
        registers[reg1] += registers[reg2]  # Perform addition
    elif opcode == "STORE":
        reg, address = operands[0], int(operands[1])  # Extract register and address
        print(f"Value at Memory Address {address}: {registers[reg]}")
    else:
        print("Unknown instruction")

# Fetch-Decode-Execute Cycle
while (pc < len(memory)):
    instruction = memory[pc]  # Fetch
    print(f"Fetched Instruction: {instruction}")
    opcode, operands = decode(instruction)  # Decode
    print(f"Decoded Instruction: Opcode = {opcode}, Operands = {operands}")
    execute(opcode, operands)  # Execute
    print(f"Registers after execution: {registers}\n")
    pc += 1  # Update Program Counter to the next instruction
