#Python3.8.1
# Search a value into the vectors, using binary search

def binary_search(list, find):
    down = 0
    high = len(list) - 1 # because of vetor that initiate in zero
    while down <= high:
        middle = int((down + high)/2)
        compare  = list[middle]
        print("Place of minor vector " + str(down))
        print("Place of larger vector " + str(high))
        print("Place of middle vector ", str(middle))
        print("Value than you are searching" ,find, "and " "Value current in the middle vector", compare, "\n") 
        if compare == find:
            return (middle)
        if compare > find:
            high = middle - 1
        else:
            down = middle + 1
    return None

list = [1, 3, 5, 7, 9]
binary_search(list, 1)
