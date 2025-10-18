def partition(arr,low,high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i+=1
    arr[high], arr[i] = arr[i], arr[high]
    return i

def quick_sort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

if __name__ == "__main__":
    sample_array = [64, 25, 12, 22, 11, 90]
    n = len(sample_array)
    
    quick_sort(sample_array, 0, n - 1)
    
    print("Sorted array:", sample_array)