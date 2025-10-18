def heapify(arr, n, root):
    largest = root
    left = root*2+1
    right = root*2+2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr,n,largest)

def heap_sort(arr):
    n = len(arr)
    lastParents = n // 2 - 1
    for i in range(lastParents, -1, -1):
        heapify(arr,n,i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == "__main__":
    sample_array = [64, 25, 12, 22, 11, 90]
    
    heap_sort(sample_array)
    
    print("Sorted array:", sample_array)