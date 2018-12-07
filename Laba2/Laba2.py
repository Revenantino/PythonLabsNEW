def main():
    list_of_lines = []
    f = open("textLABA2.txt", "r")
    f1 = f.readlines()
    for x in f1:
        print(x)
        list_of_lines.append(x)
    print("--------------------------------------------------------------------------------------------------------------")
    print(list_of_lines)
    print("--------------------------------------------------------------------------------------------------------------")
    f.close()


def task2():
    f2 = open("a.txt.txt", encoding='utf-8')
    fb1 = open("b1", "w")
    fb2 = open("b2", "w")
    f3 = f2.readlines()
    h = 0
    for line in f3:
        h += 1
        if h % 2 == 0:
            line.upper()
            fb1.write(line)
        else:
            line.lower()
            fb2.write(line)
        x2 = line.split("/n")
        print(x2)
    print(h)


if __name__ == '__main__':
    main()
    task2()
