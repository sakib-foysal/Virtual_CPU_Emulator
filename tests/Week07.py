
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
    

# Week 7: Advanced Features
def week_7_advanced_features():
    """
    Week 7: Implement branching, subroutines, and simple pipelining.
    """
    
    assembler = instraction_formating()  # Call instruction_formating to get assembler function
    
    # Example assembly instructions
    assembly_instructions = ["BRANCH R0 5", "ADD R1 10", "HALT R0 0"]
    memory = [assembler(inst) for inst in assembly_instructions]
    
    registers = [0b000000] * 4
    pc = 0  # Program counter
    
    def execute(instruction):
        nonlocal pc
        opcode = instruction[:4]
        if opcode == "0110":  # Branch to address
           pc = int(instruction[4:].replace(" ", ""), 2)  # Strip extra spaces before converting
        elif opcode == "0001":  # ADD
            reg_num = int(instruction[4:6], 2)
            value = int(instruction[6:], 2)
            registers[reg_num] += value

    # Pipeline: Fetch, Decode, Execute
    pipeline = {"fetch": None, "decode": None, "execute": None}
    while pc < len(memory):
        pipeline["execute"] = pipeline["decode"]
        pipeline["decode"] = pipeline["fetch"]
        pipeline["fetch"] = memory[pc]
        if pipeline["execute"]:
            execute(pipeline["execute"])
        pc += 1
    return [f"R{i}: {reg:06b}" for i, reg in enumerate(registers)]





# Execute all new functions and collect their outputs
outputs = {
    "week_7_advanced_features": week_7_advanced_features()
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

