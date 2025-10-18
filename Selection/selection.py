def partition(arr,low,high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i+=1
    arr[high], arr[i] = arr[i], arr[high]
    return i

def selection(arr,low,high,k):
    if low<=high:
        pi = partition(arr,low,high)
        if k == pi+1:
            return arr[pi]
        elif k < pi+1:
            return selection(arr,low,pi-1,k)
        else:
            return selection(arr,pi+1,high,k)
    return -1

if __name__ == "__main__":
    sample_array = [64, 25, 12, 22, 11, 90]
    result = selection(sample_array,0,len(sample_array)-1,2)
    print(f"2번째로 작은 값은 {result}")