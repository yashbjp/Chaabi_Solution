def switchKeyWithVaue(dict_to_swap):
    res = dict((v,k) for k,v in dict_to_swap.items())
    return res


dict_to_swap = {}

length = int(input())

while len(dict_to_swap) < length:
    input_keys = input("Enter key: ")
    input_values = input("Enter value: ")

    dict_to_swap[input_keys] = input_values
answer=switchKeyWithVaue(dict_to_swap)
print(answer )