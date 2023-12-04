# inheritance vs composition in python

class CPU:
    def __init__(self,cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self,size) -> None:
        self.size = size

class HardDisk:
    def __init__(self,capacity) -> None:
        self.capacity = capacity

# computer has a cpu
# computer has a ram
# computer has a hardDisk
class Computer:
    def __init__(self,cpu_cores,ram_size, hd_capacity) -> None:
        self.cpu = CPU(cpu_cores)
        self.ram = RAM(ram_size)
        self.hard_disk = HardDisk(hd_capacity)


hp = Computer(8, 8, 512)
