def main():
    a = int(input());
    b = int(input());
    arr = []
    simpledigits(a,b,arr)
    if len(arr) != 0:
        print(arr)

def simpledigits(a,b,arr):
    try:
        if a < 0 or b < 0:
            exit(1)
        for num in range(a, b + 1):
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    arr.append(num)
        if len(arr) == 0:
            exit(1)

    except:
       raise Exception("NoSimpleDigits")

    return arr
