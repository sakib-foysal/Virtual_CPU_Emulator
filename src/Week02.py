#Week 2: Instruction Set Architecture (ISA)
#Task: Create a simple assembler to convert assembly code into machine code.


instruction_set = {
    "ADD": "0001",
    "SUB": "0010",
    "LOAD": "0011",
    "STORE": "0100",
    "MOV": "0101",
    "AND": "0110",
    "OR": "0111",
    "JMP": "1000",
    "BEQ": "1001",
    "NOP": "1010",
}


def register_to_bin(reg):
    """Convert a register name (e.g., R1) to binary."""
    return format(int(reg[1:]), '04b')


def immediate_to_bin(value):
    """Convert an immediate value to an 8-bit binary representation."""
    return format(value, '08b')


def assemble(instruction):
    """Convert a single assembly instruction into machine code."""
    parts = instruction.strip().split()
    opcode = instruction_set[parts[0]]

    if parts[0] in ["ADD", "SUB", "AND", "OR"]:
        r1 = register_to_bin(parts[1])
        r2 = register_to_bin(parts[2])
        return f"{opcode} {r1} {r2}"

    elif parts[0] in ["LOAD", "STORE"]:
        r1 = register_to_bin(parts[1])
        address = immediate_to_bin(int(parts[2]))
        return f"{opcode} {r1} {address}"

    elif parts[0] in ["JMP", "BEQ"]:
        address = immediate_to_bin(int(parts[1]))
        return f"{opcode} {address}"

    elif parts[0] == "NOP":
        return f"{opcode}"

    else:
        raise ValueError(f"Unsupported instruction: {parts[0]}")


# User input for assembly code
print("Enter your assembly code line by line (type 'END' to finish):")
user_assembly_code = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    user_assembly_code.append(line.strip())

# Assemble each line
try:
    machine_code = [assemble(line) for line in user_assembly_code if line.strip()]
    print("\nMachine Code Output:")
    print("\n".join(machine_code))
except ValueError as e:
    print(f"Error: {e}")

# Example assembly code
#assembly_code =
"""
LOAD R1 15
ADD R1 R2
STORE R1 20
JMP 10
NOP
"""