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

def writecompressedfile(input_filename, compressed_file_name, representationDict):
    f = open(input_filename, "r")
    w = open(compressed_file_name, "w")
    char = f.read(1)
    while(char != ""):
        w.write(representationDict[char])
        char = f.read(1)
    f.close()
    w.close() 

def testSolution(input_file, compressed, ReprDict):#compressed.txt, revert to ASCII, comp input
    out = open(compressed, "r")
    inputt= open(input_file, "r")

    char = out.read(1)
    while(char != ""):#char is 0
        input_file_char = inputt.read(1) #a in input_file
        while(char not in ReprDict):
            char = char + out.read(1)

        if(ReprDict[char] != input_file_char):
            return "Failed"
        char = out.read(1)
    return "Passed"

def Makebintochar(chartobin):
    newdict = {}
    for key in chartobin:#KEY = key, VALUE = chartobin[key]
        newdict[chartobin[key]] = key
    return newdict

def main():
    input_file_name = "input.txt"
    compressed_file_name = "compressed.txt"

    charCount = countDict(input_file_name)
    writeNormalFile(input_file_name)

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

    chartobin = {}
    node = parent
    runningnum = ""
    while(node != None):
        if(node.leftobj.isChar == 'T' and node.rightobj.isChar == "T"):
            chartobin[node.leftobj.alphabet] = runningnum + "0"
            chartobin[node.rightobj.alphabet] = runningnum + "1"
            node = None 
        else:
            if(node.leftobj.isChar == "T"):
                charNode = node.leftobj
                nonCharNode = node.rightobj
            else:
                charNode = node.rightobj
                nonCharNode = node.leftobj
            
            chartobin[charNode.alphabet] = runningnum + "1"
            runningnum = runningnum + "0"
            node = nonCharNode

    writecompressedfile(input_file_name, compressed_file_name, chartobin)

    testResult = testSolution(input_file_name, compressed_file_name, Makebintochar(chartobin))
    print(testResult)
main()
