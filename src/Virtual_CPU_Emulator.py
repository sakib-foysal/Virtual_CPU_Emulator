

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




# Week 3: Basic CPU Components
def week_3_cpu_components():
    """
    Week 3: Build basic CPU components: ALU, registers, and program counter.
    """
    class ALU:
        def operate(self, opcode, operand1, operand2):
            if opcode == "0001":  # ADD
                return operand1 + operand2
            elif opcode == "0010":  # SUB
                return operand1 - operand2

    class Registers:
        def __init__(self):
            self.regs = [0b000000] * 4  # Four 6-bit registers

        def write(self, reg_num, value):
            self.regs[reg_num] = value

        def read(self, reg_num):
            return self.regs[reg_num]

    alu = ALU()
    registers = Registers()
    pc = 0b000000  # Program counter

    # Example operations
    registers.write(0, 0b000010)  # Write 2 to R0
    registers.write(1, 0b000011)  # Write 3 to R1
    result = alu.operate("0001", registers.read(0), registers.read(1))  # ADD R0, R1
    main_result= f"Result of ADD: {result:06d}"
    pc_results= f"\nProgram Counter: {pc:06b}"

    return main_result + pc_results



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



# Week 5: Memory Management
def week_5_memory_management():
    """
    Week 5: Implement memory management for the virtual CPU.
    """
    memory = [0b000000] * 16  # 16 memory locations
    
    def write_memory(address, value):
        memory[address] = value

    def read_memory(address):
        return memory[address]

    # Example operations
    write_memory(2, 0b000101)  # Write value 5 to address 2
    write_memory(5, 0b001011)  # Write value 11 to address 5
    
    return [f"Address {i:0d}: {v:06b}" for i, v in enumerate(memory)]



# Week 6: I/O Operations
def week_6_io_operations():
    """
    Week 6: Implement basic I/O operations with simulated keyboard and display.
    """
    value1 = 6   #keyboard input
    value2 = 0
    
    
    io_devices = {"keyboard": bin(value1)[2:], "display": bin(value2)[2:]}
    
   
    def read_input(device):
        if device == "keyboard":
            # Simulate reading input from keyboard (e.g., entering the number 12)
           io_devices[device] = value1

    def write_output(device):
        if device == "display":
            return f"Display Output: {io_devices[device]:0d}"

    # Example I/O operations
    read_input("keyboard")
    io_devices["display"] = io_devices["keyboard"]  # Copy keyboard input to display
    return write_output("display")




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




# Week 9: Final Testing & Debugging
def week_9_testing_debugging():
    """
    Week 9: Test the emulator with various programs and validate performance.
    """
    
    
    assembler = instraction_formating()  # Call instruction_formating to get assembler function


    # Example assembly instructions
    assembly_instructions = ["ADD R1 1", "SUB R1 1", "ADD R1 1", "HALT R0 0"]
    memory = [assembler(inst) for inst in assembly_instructions]
    
    
    registers = [0b000000] * 4
    pc = 0

    def execute(instruction):
        opcode = instruction[:4]
        reg_num = int(instruction[4:6], 2)
        value = int(instruction[6:].replace(" ", ""), 2)  # Remove spaces before conversion
        if opcode == "0001":  # ADD
            registers[reg_num] += value
        elif opcode == "0010":  # SUB
            registers[reg_num] -= value

    # Fetch-Decode-Execute cycle
    while pc < len(memory):
        execute(memory[pc])
        pc += 1

    return [f"R{i}: {reg:06b}" for i, reg in enumerate(registers)]






# Execute all new functions and collect their outputs
outputs = {
    "week_2_Machine Code Output": week_2_define_instructions(),
    "week_3_cpu_components": week_3_cpu_components(),
    "week_4_execute_instructions": week_4_execute_instructions(),
    "week_5_memory_management": week_5_memory_management(),
    "week_6_io_operations": week_6_io_operations(),
    "week_7_advanced_features": week_7_advanced_features(),
    "week_8_optimization": week_8_optimization(),
     "week_9_testing_debugging": week_9_testing_debugging()  # Final testing and debugging

    
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

