

def countDict(filename):
    countDict = {}
    f = open(filename, "r")
    char = f.read(1)
    while(char != ""):
        if(char in countDict):
            countDict[char] +=1 
        else:
            countDict[char] = 1
        char = f.read(1)
    f.close()
    return countDict

class node:
    def __init__(self, value, alphabet, isChar):
        self.val = value
        self.alphabet = alphabet
        self.isChar = isChar 
        self.leftobj = None 
        self.rightobj = None 

class minHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i): 
        return (i-1)//2

    def leftchild(self, i): 
        return (i*2)+1 #left child

    def rightchild(self, i): 
        return (i*2)+2 #right child

    def hasrightChild(self,index):
        rightchildindex = self.rightchild(index)
        if(rightchildindex >= len(self.heap)):
            return False
        return True 

    def hasleftChild(self,index):
        leftchildindex = self.leftchild(index)
        if(leftchildindex >= len(self.heap)):
            return False
        return True 

    def insert(self, value):
        self.heap.append(value)
        self.heapify(len(self.heap), "I")

    def extract(self):
        if(len(self.heap) == 0):
            return "Error extracting from empty heap"
        elif(len(self.heap) == 1):
            firstelem = self.heap[0]
            del self.heap[0]
            return firstelem
        min_element = self.heap[0]
        last_elem_index = len(self.heap) -1 #1, 2...
        self.heap[0] = self.heap[last_elem_index]
        del self.heap[last_elem_index]
        self.heapify(len(self.heap), "E")
        return min_element

    def heapify(self, length, op):
        if(length == 1 or length ==0):
            return 
        else:
            if(op == 'I'):
                childIndex = length -1 #1
                parentIndex = self.parent(childIndex) #0
                while(childIndex != 0 and self.heap[childIndex].val < self.heap[parentIndex].val):
                    smallernumobj = self.heap[childIndex]
                    self.heap[childIndex] = self.heap[parentIndex]
                    self.heap[parentIndex] = smallernumobj

                    childIndex = parentIndex 
                    parentIndex = self.parent(childIndex)
                return
            else:
                parentIndex = 0 

                while(self.hasleftChild(parentIndex)):
                    smallerChildIndex = self.leftchild(parentIndex)
                    if(self.hasrightChild(parentIndex) == True):
                        RightChildIndex = self.rightchild(parentIndex)
                        if(self.heap[RightChildIndex].val < self.heap[smallerChildIndex].val):
                            smallerChildIndex = RightChildIndex
                    if(self.heap[parentIndex].val < self.heap[smallerChildIndex].val):
                        break
                    else:
                        savedVal = self.heap[smallerChildIndex] 
                        self.heap[smallerChildIndex] = self.heap[parentIndex]
                        self.heap[parentIndex] = savedVal
                        parentIndex = smallerChildIndex
