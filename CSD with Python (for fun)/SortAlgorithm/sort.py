'''              
Selection Sort
Time complexity: O(n^2) (best case, average case, worst case)
Space complexity: O(1)
'''
def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

'''
Bubble Sort
Time complexity: O(n) (best case), else, O(n^2)
Space complexity: O(1)
'''
def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

'''
Insertion sort
Time complexity and space complexity same as bubble sort
'''
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and  key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

'''
Heap sort
Time complexity: O(n log(n)) for all cases 
'''
def heap(arr, n, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < n and arr[index] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heap(arr, n, largest)

def heapSort(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        heap(arr, len(arr), i)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, i, 0)
'''
Quick sort
Time complexity: O(n log(n)) for best and average cases, O(n^2) for worst cases
'''
def divide(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low = None, high = None):
    if len(arr) == 1:
        return arr
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = divide(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)

'''
Merge sort 
Time complexity: O(n log(n)) in all cases
'''
def merge(arr, left, mid, right):
    x = mid - left + 1
    y = right - mid
    # temp lists
    L = [0] * x
    R = [0] * y
    # copy elements to temp lists
    for i in range(0, x):
        L[i] = arr[left + i]
    for j in range(0, y):
        R[j] = arr[mid + 1 + j]
    # merge temp lists into list arr[left..right]
    i, j, k = 0, 0, left
    while i < x and j < y:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # copy remaining elements of L[] or R[] if there are many
    while i < x:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < y:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left = None, right = None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    if left < right:
        mid = left + (right - left) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

'''
Radix sort
Time complexity O(nk)
P/S should be used in large number, in numbers < 100, it run super slow
'''
def countingSort(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10
    for i in range(len(arr)):
        index = arr[i] / exp
        count[int(index % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = len(arr) - 1
    while i >= 0:
        index = arr[i] / exp
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1
    i = 0
    for i in range(len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    highest = max(arr)
    exp = 1
    while highest / exp > 0:
        countingSort(arr, exp)
        exp *= 10

if __name__ == '__main__':
    arr = [1700, 1200, 634534, 2374824, 134710, 12984234, 1381748, 1234498]
    radixSort(arr)
    print(arr[::-1])
