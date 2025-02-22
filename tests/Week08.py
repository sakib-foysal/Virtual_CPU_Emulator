
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
    


# Week 8: Performance Optimization
def week_8_optimization():
    """
    Week 8: Profile the emulator and optimize critical paths.
    """
    from time import time
    
    
    assembler = instraction_formating()  # Call instruction_formating to get assembler function


    # Example assembly instructions
    assembly_instructions = ["ADD R1 2", "SUB R1 1", "HALT R0 0"]
    memory = [assembler(inst) for inst in assembly_instructions]
    

    registers = [0b000000] * 4
    pc = 0

    def execute(instruction):
        opcode = instruction[:4]
        reg_num = int(instruction[4:6], 2)
        value = int(instruction[6:].replace(" ", ""), 2) # Remove spaces before conversion
        if opcode == "0001":  # ADD
            registers[reg_num] += value
        elif opcode == "0010":  # SUB
            registers[reg_num] -= value

    # Profile the emulator
    start_time = time()
    while pc < len(memory):
        execute(memory[pc])
        pc += 1
    end_time = time()

    return f"Execution Time: {end_time - start_time:.6f} seconds",[f"R{i}: {reg:06b}" for i, reg in enumerate(registers)]




# Execute all new functions and collect their outputs
outputs = {
    "week_8_optimization": week_8_optimization() 
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

