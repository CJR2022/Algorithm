def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    sample_array = [64, 25, 12, 22, 11]
    sorted_array = bubble_sort(sample_array)
    print("Sorted array:", sorted_array)
