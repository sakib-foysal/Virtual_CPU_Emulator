# Virtual_CPU_Emulator
<img src="https://github.com/sakib-foysal/Virtual_CPU_Emulator/blob/main/images/cpu.png" height="200" /><img src="https://github.com/sakib-foysal/Virtual_CPU_Emulator/blob/main/images/cpu_architecture.png" height="200"/>

## Project Description 📝
This project builds a Virtual CPU Emulator to simulate essential CPU components and operations. It covers Instruction Set Architecture (ISA), ALU, memory management, and I/O operations, following a **10-week** structured plan.
## Group Members 👥
- Member 1: [Sakib Foysal Ejarder **ID: 11220320948**](mailto:sakibfoysal2@gmail.com)
- Member 2: [Sayed Tauhidul Islam **ID: 11220320950**](mailto:itouhidul322@gmail.com)
- Member 3: [Juena Tabassum **ID: 11220320982**](mailto:juenatabassum01@gmail.com)

**Overview:** This project builds a Virtual CPU Emulator to simulate essential CPU components and operations. It covers Instruction Set Architecture (ISA), ALU, memory management, and I/O operations, following a 10-week structured plan.

**Goals:** 
  1. Develop a virtual CPU with core functionalities.
  2. Implement basic instructions (ADD, SUB, LOAD, STORE).
  3. Create a testing environment for assembly programs.

## Objective 🎯
The Virtual CPU Emulator is intended to be a simplified, more interactive source for learning about and experimenting with CPU architectures and the execution of their instructions. The project simulates basic CPU operations, the project aims to:
- Learning computer architecture and low-level programming.
- Allows safe experimentation with assembly and instruction set.
- Tool for debugging and analyzing instruction execution in a controlled virtual environment.
- Assisting teachers and students in visualizing and experimenting with the underlying concepts of CPU functionality.
The emulation aims not only at this but also seeks to connect theory with practice truly processors work in fundamentals.

## Tools 💻
- **Programming Language:** Python
- **Version Control:** GitHub
- **Development Environment:** Any Python IDE or text editor with Python

## Weekly Tasks Overview 🗓️

### [Week 1: Project Planning & Setup](https://github.com/sakib-foysal/Virtual_CPU_Emulator/blob/main/docs/Week%2001.pdf)
- **Tasks:**
  - Outline the features of the virtual CPU.
  - Choose a programming language (Python/C++) and tools.
  - Set up version control (e.g., GitHub).

### [Week 2: Instruction Set Architecture (ISA)]
- **Tasks:**
  - Define basic instructions (ADD, SUB, LOAD, STORE, etc.).
  - Document the instruction formats.
  - Create a simple assembler to convert assembly code into machine code.

## Instructions Formatting

### 1. Opcode Mapping
- A dictionary stores instruction opcodes as binary strings.

### 2. Assembler Function (`assembler`)
- Splits an instruction string (e.g., `"ADD R1 10"`) into parts.
- Converts the opcode to its binary representation.
- Extracts the register number (e.g., `R1 → 0001`).
- Converts the numeric value (if present) to an 8-bit binary string.

### 3. Return Value
- Returns a formatted binary instruction string.
### Example usage
```python
 assembler = instraction_formating()
 print(assembler("ADD R1 10"))    # Output: "0001 0001 00001010"
 print(assembler("HALT R0 0"))    # Output: "1111 0000 00000000"
 print(assembler("BRANCH R0 5"))  # Output: "0110 0000 00000101"
```
### How It Works:

1. **Calls `instruction_formatting()`**
   - Retrieves the `assembler` function that translates assembly instructions into binary machine code.

2. **Defines Example Assembly Instructions**
   - A list of instructions like `"ADD R1 10"`, `"SUB R2 5"`, etc.

3. **Converts Instructions to Machine Code**
   - Iterates over instructions, calling `assembler()` on each, and stores the results in `machine_code`.

4. **Returns Machine Code**
   - The function returns a list of binary representations of the instructions.

### Example Output:

```python
# Running the function
print(week_2_define_instructions())

# Output:
["0001 0001 00001010",  # ADD R1 10
 "0010 0010 00000101",  # SUB R2 5
 "0011 0001 00010100",  # LOAD R1 20
 "0100 0010 00001111"   # STORE R2 15]
```

### [Week 3: Basic CPU Components]
- **Tasks:**
  - Build the ALU (Arithmetic Logic Unit).
  - Implement general-purpose registers.
  - Create the program counter and instruction register.
    
### Key Components:

1. **ALU (Arithmetic Logic Unit)**  
   - A class that performs basic operations (ADD, SUB) based on the opcode provided.  
   - For example, `0001` for addition (ADD) and `0010` for subtraction (SUB).

2. **Registers**  
   - A class with four 6-bit registers (initialized to `0b000000`), where you can read or write values to specific registers.

3. **Program Counter (PC)**  
   - This tracks the memory location of the next instruction to be executed (here it is initialized to `0b000000`).

### Workflow:

1. Two values (2 and 3) are written into registers `R0` and `R1`.
2. The ALU performs an ADD operation on these two values (2 + 3).
3. The result of the ADD operation is stored and returned as a 6-bit number (`000010`).
4. The Program Counter value (`000000`) is also included in the return result.

### Code

```python
def week_3_cpu_components():
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
```
### [Week 4: Instruction Execution]
- **Tasks:**
  - Implement the instruction fetching mechanism.
  - Decode instructions and execute them using the ALU and registers.
  - Test with simple programs.
### Key Components:

1. **Memory**  
   A list of instructions in string format, which would normally be fetched from memory in a CPU.

2. **Registers**  
   A dictionary with initial values representing the state of some CPU registers.

3. **Program Counter (PC)**  
   A counter that keeps track of the current instruction's position in memory.

### Fetch-Decode-Execute Cycle:

1. **Fetch**  
   An instruction is fetched from memory using the Program Counter (PC).

2. **Decode**  
   The instruction is split into the operation (opcode) and its operands (e.g., registers or values).

3. **Execute**  
   The operation is performed based on the opcode, updating registers or memory accordingly.

### Functions:

- **decode**  
  This function splits the instruction into the operation and operands.

- **execute**  
  Executes the operation. For example:
  - `LOAD` puts a value into a register.
  - `ADD` adds two registers.
  - `STORE` outputs the value from a register to memory.

### Workflow:
1. The program starts with a memory array of instructions.
2. For each instruction:
   - It is fetched from memory.
   - It is decoded to extract the opcode and operands.
   - The operation is executed, modifying the registers.
3. The Program Counter (PC) increments, and the cycle repeats until all instructions are executed.

### Code:

```python
    # Function to decode an instruction
    def decode(instruction):
        parts = instruction.split()  # Split into operation and operands
        opcode = parts[0]  # The operation (e.g., LOAD, ADD, STORE)
        operands = parts[1:]  # The arguments (e.g., R1, 10)
        return opcode, operands
```
### Output:

The function returns a list containing:
- Fetched instruction.
- Decoded instruction (opcode and operands).
- The state of the registers after executing the instruction.

### [Week 5: Memory Management]
- **Tasks:**
  - Set up a simulated memory space.
  - Implement memory read/write operations.
  - Handle address mapping and memory segmentation.

The `week_5_memory_management()` function simulates memory management for a virtual CPU. It initializes a list of memory with 16 locations, each initialized to zero. The function also defines two helper functions:

1. **write_memory(address, value)**  
   This function writes a binary value to a specific memory address.

2. **read_memory(address)**  
   This function returns the value stored at a given memory address.

### Example Workflow:

- The function writes the binary values `0b000101` (which is `5` in decimal) and `0b001011` (which is `11` in decimal) to memory addresses `2` and `5`, respectively.
  
- After performing the memory operations, the function returns a formatted list of memory locations, showing each address and its stored binary value, ensuring a 6-bit representation for each value.
  
### Code

```python
    def write_memory(address, value):
        memory[address] = value

    def read_memory(address):
        return memory[address]
```
### Week 6: I/O Operations
- **Tasks:**
  - Implement simulated I/O devices (keyboard, display).
  - Create I/O instructions and integrate them with the CPU.
  - Test with I/O-intensive programs.

The `week_6_io_operations()` function simulates basic input/output (I/O) operations, specifically handling input from a "keyboard" and output to a "display." The function performs the following:

1. **Simulated Keyboard Input**  
   It reads a value (in this case, `6`) from the "keyboard" and stores it in a dictionary.
   
2. **Display Output**  
   The value from the "keyboard" is transferred to the "display" device, and the output is returned as a formatted string.

### Code Snippet (Week 6):

```python
    def read_input(device):
        if device == "keyboard":
            io_devices[device] = value1

    def write_output(device):
        if device == "display":
            return f"Display Output: {io_devices[device]:0d}"

    read_input("keyboard")
    io_devices["display"] = io_devices["keyboard"]
    return write_output("display")
```
### Week 7: Advanced Features
- **Tasks:**
  - Implement branching and control flow instructions.
  - Add support for subroutines and interrupts.
  - Integrate a simple pipeline mechanism.

This week, we simulate an emulator that supports branching, subroutine execution, and a basic pipeline (fetch, decode, execute). The assembly instructions are formatted, and the program counter (pc) handles the branching logic. The program simulates a basic pipeline, where each instruction is processed sequentially.

### Key Features:
- **Branching:** The emulator handles branch instructions (`BRANCH`) that modify the flow of execution based on register values.
- **Subroutine Execution:** The program executes instructions like `ADD` and `HALT`, affecting the registers.
- **Pipeline:** The program implements a basic pipeline, processing each instruction in three stages: fetch, decode, and execute.

### Code

```python
    pc = 0
    pipeline = {"fetch": None, "decode": None, "execute": None} 
    while pc < len(memory):
        pipeline["execute"] = pipeline["decode"]
        pipeline["decode"] = pipeline["fetch"]
        pipeline["fetch"] = memory[pc]
        if pipeline["execute"]:
            execute(pipeline["execute"])
        pc += 1
```
### Week 8: Performance Optimization
- **Tasks:**
  - Profile the emulator to identify bottlenecks.
  - Optimize critical code paths.
  - Enhance the assembler for better instruction encoding.
### Week 8: Execution Time Profiling and Optimization

In Week 8, the emulator is enhanced by profiling its execution time. The program now measures how long it takes to execute the cycle of instructions and calculates the execution time. Additionally, it returns the register states after execution.

### Key Features:
- **Execution Time Profiling:** The program tracks the start and end times of the instruction cycle and calculates the total execution time.
- **Optimization:** The cycle of instructions is executed, and the program measures the time taken for each instruction to run.

### Code

```python
    from time import time
    registers = [0b000000] * 4
    pc = 0
    start_time = time()
    while pc < len(memory):
        execute(memory[pc])
        pc += 1
    end_time = time()
```
### Week 9: Final Testing & Debugging
- **Tasks:**
  - Test with a variety of assembly programs.
  - Debug and fix any issues.
  - Validate performance against benchmarks.

In Week 9, the function simulates the final phase of testing and debugging. It runs a set of assembly instructions through the emulator, executing each one step-by-step. After all instructions are processed, it returns the final state of the registers.

### Key Features:
- **Instruction Execution:** The function processes each instruction sequentially in the emulator.
- **Final Register State:** After the execution of all instructions, the final state of the registers is returned.

### Code

```python
    registers = [0b000000] * 4
    pc = 0
    while pc < len(memory):
        execute(memory[pc])
        pc += 1
```
### Week 10: Documentation & Presentation
- **Objective:** Document the project and prepare for presentation.
- **Tasks:**
  - Write comprehensive documentation.
  - Prepare a project report and presentation slides.
  - Conduct a demo session.
**Collaboration:** Our team uses GitHub for version control and progress tracking.
