def compress(charstream, verbose=False):
    d = {}
    p = ""
    codestream = []
    i = 0
    while True:
        c = charstream[i]
    try:
        d[p + c]
        p = p + c
    except (KeyError):
     if p == "":
        o = 0
     else:
        try:
            o = d[p]
        except (KeyError):
            print("Error")
            exit(1)
     codestream.append((o, c))
     d[p + c] = len(d) + 1
     p = ""
     i += 1
     if i < len(charstream):
        continue
     else:
       if p != "":
           codestream.append((d[p], 0))
        break
     output = ""
     for block in codestream:
        for part in block:
            output += str(part)
     return codestream


n = input()
a = compress(str(n))
print(a)
