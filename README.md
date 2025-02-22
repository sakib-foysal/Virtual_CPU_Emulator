# Virtual_CPU_Emulator
<img src="https://github.com/sakib-foysal/Virtual_CPU_Emulator/blob/main/images/cpu.png" height="200" /><img src="https://github.com/sakib-foysal/Virtual_CPU_Emulator/blob/main/images/cpu_architecture.png" height="200"/>

## Project Description 📝
This project builds a Virtual CPU Emulator to simulate essential CPU components and operations. It covers Instruction Set Architecture (ISA), ALU, memory management, and I/O operations, following a 10-week structured plan.
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
- **Objective:** Define project scope, gather resources, and set up a development environment.
- **Tasks:**
  - Outline the features of the virtual CPU.
  - Choose a programming language (Python/C++) and tools.
  - Set up version control (e.g., GitHub).

### [Week 2: Instruction Set Architecture (ISA)]
- **Objective:** Design the ISA for the virtual CPU.
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
- **Objective:** Implement core components of the CPU.
- **Tasks:**
  - Build the ALU (Arithmetic Logic Unit).
  - Implement general-purpose registers.
  - Create the program counter and instruction register.

### [Week 4: Instruction Execution]
- **Objective:** Develop the instruction fetch-decode-execute cycle.
- **Tasks:**
  - Implement the instruction fetching mechanism.
  - Decode instructions and execute them using the ALU and registers.
  - Test with simple programs.

### [Week 5: Memory Management]
- **Objective:** Implement memory management for the virtual CPU.
- **Tasks:**
  - Set up a simulated memory space.
  - Implement memory read/write operations.
  - Handle address mapping and memory segmentation.

### Week 6: I/O Operations
- **Objective:** Enable basic input/output operations.
- **Tasks:**
  - Implement simulated I/O devices (keyboard, display).
  - Create I/O instructions and integrate them with the CPU.
  - Test with I/O-intensive programs.

### Week 7: Advanced Features
- **Objective:** Add advanced CPU features.
- **Tasks:**
  - Implement branching and control flow instructions.
  - Add support for subroutines and interrupts.
  - Integrate a simple pipeline mechanism.

### Week 8: Performance Optimization
- **Objective:** Optimize the emulator for better performance.
- **Tasks:**
  - Profile the emulator to identify bottlenecks.
  - Optimize critical code paths.
  - Enhance the assembler for better instruction encoding.

### Week 9: Final Testing & Debugging
- **Objective:** Thoroughly test and debug the emulator.
- **Tasks:**
  - Test with a variety of assembly programs.
  - Debug and fix any issues.
  - Validate performance against benchmarks.

### Week 10: Documentation & Presentation
- **Objective:** Document the project and prepare for presentation.
- **Tasks:**
  - Write comprehensive documentation.
  - Prepare a project report and presentation slides.
  - Conduct a demo session.
**Collaboration:** Our team uses GitHub for version control and progress tracking.
