
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



# Execute all new functions and collect their outputs
outputs = {
    "week_3_cpu_components": week_3_cpu_components()
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
