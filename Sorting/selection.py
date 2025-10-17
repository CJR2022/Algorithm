def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
# Example usage:
if __name__ == "__main__":
    sample_array = [64, 25, 12, 22, 11]
    sorted_array = selection_sort(sample_array)
    print("Sorted array:", sorted_array)
            