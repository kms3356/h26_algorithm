def merge_sort(nums, left, right):
    if left >= right: return
    mid = (left+right) // 2
    merge_sort(nums,left,mid)
    merge_sort(nums, mid+1,right)
    merge(nums, left,mid,right)

def merge(nums,left,mid,right):
    i = k = left
    j = mid+1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            sorted_list[k] = nums[i]
            i += 1
        else:
            sorted_list[k] = nums[j]
            j += 1
        k += 1
    if i <= mid:
        sorted_list[k:right+1] = nums[i:mid+1]
    elif j <=right:
        sorted_list[k:right+1] = nums[j:right+1]
    nums[left:right+1] = sorted_list[left:right+1]

nums = list(map(int,input().split()))
sorted_list = [0] * len(nums)
merge_sort(nums, 0,len(nums)-1)
print(nums)