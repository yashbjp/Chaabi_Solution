def columnSorting(arr,key_to_sort):
    ans=sorted(arr, key=lambda x: x[key_to_sort])
    return ans


array_of_dict=[
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
]

key_to_sort=input()
answer=columnSorting(array_of_dict,key_to_sort)
print(answer)