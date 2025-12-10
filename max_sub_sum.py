def sum_sub(arr):
    max_sum=arr[0]
    current_sum=arr[0]
    for i in arr[1:]:
        current_sum=max(i,current_sum+i)
        max_sum=max(current_sum,max_sum)
    return max_sum
arr=[1,2,3,4,5]
print(sum_sub(arr))    