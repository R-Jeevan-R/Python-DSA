'''Array -- Is a Homogeous Linear DataStructure stores elements in contigous memory locations.'''

class Array():
    def __init__(self, array = []):
        self.array = array
    
    #Time Complexity -- O(n)
    def insert_at_beginning(self, value):
        temp = Array()
        temp.insert_at_end(value)
        for i in  range(1, len(self.array) + 1):
            temp.insert_at_end(self.array[i - 1])
        self.array = temp.array

    #Time Complexity -- O(n)
    def insert_at_end(self, value):
        temp = [None]*(len(self.array) + 1)
        for i in range(len(self.array)):
            temp[i] = self.array[i]
        temp[-1] = value
        self.array = temp

    #Time Complexity -- O(n)
    def insert_at_index(self, index, value):
        if index <= -1:
            index = len(self.array) + index
        if index >= len(self.array) or index < 0:
            print('Index Out of Range')
            return
        temp = Array()
        for i in range(index):
            temp.insert_at_end(self.array[i])
        temp.insert_at_end(value)
        for i in range(index + 1, len(self.array) + 1):
            temp.insert_at_end(self.array[i - 1])
        self.array = temp.array

    #Time Complexity -- O(n)
    def pop(self, index = -1):
        if index <= -1:
            index = len(self.array) + index
        if index >= len(self.array) or index < 0:
            print('Index Out of Range')
            return
        temp = Array()
        for i in range(index):
            temp.insert_at_end(self.array[i])
        for i in range(index + 1, len(self.array)):
            temp.insert_at_end(self.array[i])
        p = self.array[index]
        self.array = temp.array
        return p

    #Time Complexity -- O(n)
    def remove(self, value):
        temp = Array()
        flag = 0
        for el in self.array:
            if flag == 0 and el == value:
                flag = 1
                continue
            temp.insert_at_end(el)
        if flag == 0:
            print(f'{value} not found in array')
            temp = None
            return
        self.array = temp.array

    #Time Complexity -- O(n + m)
    def extend(self, array, index = -1):
        if index <= -1:
            index = len(self.array) + index
        if index >= len(self.array) or index < 0:
            print('Index Out of Range')
            return
        temp = Array()
        for i in range(index + 1):
            temp.insert_at_end(self.array[i])
        for el in array:
            temp.insert_at_end(el)
        for i in range(index + 2, len(self.array) + 1):
            temp.insert_at_end(self.array[i - 1])
        self.array = temp.array

