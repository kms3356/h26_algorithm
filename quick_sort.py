def quick_sort(left,right):
    if left >=right : return
    p = partition(left,right)
    quick_sort(left, p-1)
    quick_sort(p+1,right)
    

def partition(left,right):
    pivot = A[left]
    low = left+1
    high = right

    while low <= high:
        while A[low] < pivot: 
            low += 1
            if low > right: break
        while A[high] > pivot: 
            high -=1

        if low < high:
            A[low], A[high] = A[high], A[low]
    A[left],A[high] = A[high], A[left]
    return high

A = [6,0,5,7,23,14,9,3,59,1]
quick_sort(0,len(A)-1)
print(A)