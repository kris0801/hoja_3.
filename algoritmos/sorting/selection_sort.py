def SelectionSort(arr):
    
    for i in range(len(arr)):

        min_i = i
        for j in range(i + 1, len(arr)):

            if arr[j] < arr[min_i]:
                min_i = j
        arr[i] , arr[min_i] = arr[min_i], arr[i]
        
    return arr
'''
print(SelectionSort([3, 6, 6, 6, 30, 100, -50]))
'''