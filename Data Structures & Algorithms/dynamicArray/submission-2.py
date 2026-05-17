class DynamicArray:
    def __init__(self, capacity: int):
        # Initializing based on the user-provided capacity
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        # Assuming i is valid per instructions
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # Assuming i is valid per instructions
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # If the 'parking garage' is full, we double it
        if self.size == self.capacity:
            self.resize()
        
        # Place the new element at the next available index
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # 1. Grab the last element (index is size - 1)
        val = self.arr[self.size - 1]
        # 2. Update size (conceptually 'removing' it)
        self.size -= 1
        return val

    def resize(self) -> None:
        # 1. Double the capacity tracker
        self.capacity *= 2
        # 2. Build the new, larger garage
        new_arr = [0] * self.capacity
        # 3. Copy everything from the old array to the new one
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        # 4. Swap the old garage for the new one
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
