
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



# Execute all new functions and collect their outputs
outputs = {
    "week_6_io_operations": week_6_io_operations()
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

