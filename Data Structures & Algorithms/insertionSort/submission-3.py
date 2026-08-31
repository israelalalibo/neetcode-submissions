# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key 
        self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # Take given arrays
        if not pairs:
            return []

        result = [pairs.copy()]

        for i in range(1, len(pairs)): 
            current = pairs[i] #set current to the second item in array
            j = i - 1  #set j to the item before current (first item)

            while j >= 0 and pairs[j].key > current.key:  #check if item to the left (j) is larger than the current item (current)
                pairs[j + 1] = pairs[j]  #if true move element in j position one step right
                j -= 1   #decrement j to compare with the next item to the left

            pairs[j + 1] = current   #place current into empty space (by this point the while loop is finished meaning we have either 
                                     #reached the start of the array or there are no more number to the left bigger than current

            result.append(pairs.copy())   #add the current snapshot of the list to result as asked by the

        return result

        # Sort by the size of current index

        # Outout sorted array

