#Instraction formating
def instraction_formating():
    isa = {
        "ADD": "0001",  # Opcode for addition
        "SUB": "0010",  # Opcode for subtraction
        "LOAD": "0011",  # Opcode for loading from memory
        "STORE": "0100",  # Opcode for storing to memory
        "BRANCH": "0110",  # Opcode for branching to memory
        "HALT": "1111",    # Opcode for halting to memory
    }

    def assembler(instruction):
        parts = instruction.split()
        opcode = isa[parts[0]]
        reg = f"{int(parts[1][-1]):04b} "  # Register in binary (e.g., R1 -> 01)
        value = f"{int(parts[2]):08b}" if len(parts) > 2 else "000000"  # Value in binary
        return opcode +" "+ reg + value
    
    
    
    return assembler
    # Example assembly instructions
    #assembly_instructions = ["BRANCH R0 5", "ADD R1 10", "HALT R0 0"]
    #memory = [assembler(inst) for inst in assembly_instructions]
    



# Week 2: Instruction Set Architecture (ISA)
def week_2_define_instructions():
    """
    Week 2: Define ISA and create an assembler to convert assembly to machine code.
    """
    assembler = instraction_formating()  # Call instruction_formating to get assembler function

    # Example assembly instructions
    instructions = ["ADD R1 10", "SUB R2 5", "LOAD R1 20", "STORE R2 15"]
    machine_code = [assembler(inst) for inst in instructions]
    return machine_code


# Execute all new functions and collect their outputs
outputs = {
    "week_2_Machine Code Output": week_2_define_instructions()
    
}

# Display the outputs
for key, value in outputs.items():
    print(f"{key}:\n")
    if isinstance(value, list):
        for item in value:
            print(item)
    else:
        print(value)
    print("\n")


