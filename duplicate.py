def duplicate(arr):
    seen=set()
    result=[]
    for i in arr:
        if i not in seen:
            result.append(i)
        seen.add(i)
    return result
arr=[1,2,1,3,4,4]
print(duplicate(arr))        