def merge(arr, L, R):
    i=j=k=0
    while i<len(L) and j<len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    while i<len(L):
        arr[k] = L[i]
        i+=1
        k+=1
    while j<len(R):
        arr[k] = R[j]
        j+=1
        k+=1

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(arr,L,R)
    return arr

if __name__ == "__main__":
    sample_array = [64, 25, 12, 22, 11]
    sorted_array = merge_sort(sample_array)
    print("Sorted array:", sorted_array)