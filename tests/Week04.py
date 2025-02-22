
# Week 4: Instruction Execution
def week_4_execute_instructions():
    """
    Week 4: Implement fetch-decode-execute cycle.
    """
    memory = [ "LOAD R1, 10", "ADD R1, R2", "STORE R1, 20" ] #["000101001010", "001010000001", "111100000000"]  # Binary instructions in memory
    #registers = [0b000000] * 4
    registers = {"R1": 0b00, "R2": 0b101}  # Initialize registers
    pc = 0  # Program counter
    
    
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

    main_result= []
    # Fetch-Decode-Execute Cycle
    while (pc < len(memory)):
        instruction = memory[pc]  # Fetch
        a1=f"Fetched Instruction: {instruction}"
       # print(f"Fetched Instruction: {instruction}")
        opcode, operands = decode(instruction)  # Decode
        b1=f"\nDecoded Instruction: Opcode = {opcode}, Operands = {operands}"
       # print(f"Decoded Instruction: Opcode = {opcode}, Operands = {operands}")
        execute(opcode, operands)  # Execute
        c1=f"\nRegisters after execution: {registers}"
      # print(f"Registers after execution: {registers}\n")
        pc += 1  # Update Program Counter to the next instruction
        
        main_result.append(a1)
        main_result.append(b1)
        main_result.append(c1)
        
  
    return  main_result



# Execute all new functions and collect their outputs
outputs = {
    "week_4_execute_instructions": week_4_execute_instructions()
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

