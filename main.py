from helper import countDict
from helper import node
from helper import minHeap

#change file of words to a min heap 
#extract two elements at first, make them child of a parent node and return paretn
#while heap not empty, grab one from heap and returned parent node and keep going up, form a tree 


def insertCountinHeap(charCountDict, heap):
    for key in charCountDict:#key = A, value=30
        charnode = node(charCountDict[key], key, 'T')
        heap.insert(charnode)
    return heap

def mergeTwochild(child1, child2):
    parentnode = node(child1.val+child2.val, " ", "F")

    parentnode.leftobj = child1
    parentnode.rightobj = child2
    return parentnode

def writeNormalFile(filename):
    f = open(filename, "r")
    w = open("conversion.txt", "w")
    char = f.read(1)
    while(char != ""):
        w.write(format(ord(char), 'b')) 
        char = f.read(1)
    f.close()
    w.close() 

def writecompressedfile(filename, representaionDict):
    f = open(filename, "r")
    w = open("compressed.txt", "w")
    char = f.read(1)
    while(char != ""):
        w.write(representaionDict[char])
        char = f.read(1)
    f.close()
    w.close() 

def main():
    input_file = "input.txt"
    charCount = countDict(input_file)
    writeNormalFile(input_file)

    print(charCount)
    heap = minHeap()
    heap = insertCountinHeap(charCount, heap)
    
    child1 = heap.extract() 
    child2 = heap.extract() 

    parent = mergeTwochild(child1, child2)
    while(heap.heap != []):
        child1 = heap.extract() 
        child2 = parent 
        parent = mergeTwochild(child1, child2)

    representationDict = {}
    node = parent
    runningnum = ""
    while(node != None):
        if(node.leftobj.isChar == 'T' and node.rightobj.isChar == "T"):
            representationDict[node.leftobj.alphabet] = runningnum + "0"
            representationDict[node.rightobj.alphabet] = runningnum + "1"
            node = None 
        else:
            if(node.leftobj.isChar == "T"):
                charNode = node.leftobj
                nonCharNode = node.rightobj
            else:
                charNode = node.rightobj
                nonCharNode = node.leftobj
            
            representationDict[charNode.alphabet] = runningnum + "1"
            runningnum = runningnum + "0"
            node = nonCharNode

    writecompressedfile(input_file, representationDict)
main()
