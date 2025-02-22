

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





# Execute all new functions and collect their outputs
outputs = {
    "week_5_memory_management": week_5_memory_management()  
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

