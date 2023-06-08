def sub_list(arr,first,second):
    ans=[]
    for i in range(first,second+1):
        if i%2==0:
            ans.append(arr[i])
    return ans
            


arr=[int(x) for x in input().split()]
first_index=int(input())
second_index=int(input())
answer=sub_list(arr, first_index, second_index)
print(answer)