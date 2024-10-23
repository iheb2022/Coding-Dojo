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

def values_greater_than_sec(liste1):
    if len(liste1)<2:
        return False
    else :
        newliste = []
        count=0
        for i in range(len(liste1)):
            if liste1[i]>liste1[1]:
                newliste.append(liste1[i])
                count=count+1
        print(count)
        return newliste
greater=values_greater_than_sec([6,3,2,9,0])
print(greater)

def This_length(num,repeat):
    liste = []
    for i in range(repeat):
        liste.append(num)
    return liste
len=This_length(5,3)
print(len)