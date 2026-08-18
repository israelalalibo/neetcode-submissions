class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.a = [None] * capacity
        self.size = 0


    def get(self, i: int) -> int:
        return self.a[i]

    def set(self, i: int, n: int) -> None:
        self.a[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.a[self.size] = n
        self.size += 1

    def popback(self) -> int:
        val = self.a[self.size - 1]
        self.size -= 1
        return val

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [None] * self.capacity

        for i in range(self.size):
            new_array[i] = self.a[i]

        self.a = new_array

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity