def selectionSort(array, size):
    
    for i in range(size):
        min_index = i
 
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[i], array[min_index]) = (array[min_index], array[i])
        
    return array
 
arr = [int(x) for x in input().split()]
length = len(arr)
selectionSort(arr, length)
answer=selectionSort(arr, length)
print(answer)

