class Memory:
    def __init__(self, size):

        self.size = size
        self.memory = [0] * size  # Initialize memory with zeros.

    def display_memory(self):
        #Display the contents of the memory
        for address, value in enumerate(self.memory):
            print(f"Address {address} : {value}")


    def read(self, address):

        if 0 <= address < self.size:
            return self.memory[address]
        else:
            raise ValueError("Invalid memory address.")

    def write(self, address, data):

        if 0 <= address < self.size:
            self.memory[address] = data
        else:
            raise ValueError("Invalid memory address.")


class MemoryManager:
    def __init__(self, memory, code_size, stack_size, heap_size):

        self.memory = memory
        self.code_base = 0
        self.stack_base = code_size
        self.heap_base = self.stack_base + stack_size

        if self.heap_base + heap_size > memory.size:
            raise ValueError("Memory segments exceed total memory size.")

    def map_address(self, logical_address, segment):

        if segment == 'code':
            base = self.code_base
        elif segment == 'stack':
            base = self.stack_base
        elif segment == 'heap':
            base = self.heap_base
        else:
            raise ValueError("Invalid segment name.")

        physical_address = base + logical_address
        if physical_address >= self.memory.size:
            raise ValueError("Logical address exceeds segment size.")
        return physical_address



# Initialize memory and memory manager
memory = Memory(32)
manager = MemoryManager(memory, code_size=8, stack_size=8, heap_size=16)

# Write to the code segment
code_logical_address = 10
code_physical_address = manager.map_address(code_logical_address, 'code')
#code_physical_address = manager.map_address(code_logical_address, 'stack')
#code_physical_address = manager.map_address(code_logical_address, 'heap')
memory.write(code_physical_address, 45)

# Read from the code segment
read_data = memory.read(code_physical_address)
print(f"Data at code segment address {code_logical_address} : {read_data}")

memory.display_memory()