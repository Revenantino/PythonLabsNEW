a = int(input());
b = int(input());
def boolean(a,b):
    answer = False
    try:
        if a<0 or b<0:
            exit(1)
        elif b%a == 0:
            answer = True
            return answer
        else:
            return answer
    except:
        raise Exception("Від'ємне число")
print(boolean(a,b))