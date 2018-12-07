
def flatten(l):
    output = []

    for item in l:
        if type(item) == list:
            temp = flatten(item)
            for var in temp:
                output.append(var)
        else:
            output.append(item)

    return output

a = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]
print(flatten(a))