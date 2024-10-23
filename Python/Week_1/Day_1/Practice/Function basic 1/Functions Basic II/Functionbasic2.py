def countdown():
    return list(range(5, -1, -1))
print(countdown())


def print_return(num):
    print(num[0])
    return num[1]
res= print_return([1,2])
print(res)


def first_length(first):
    return first[0] + len(first)
result=first_length([2,6,8,9])
print(result)

