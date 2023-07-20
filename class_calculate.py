n = int(input("> "))
a = 1
b = 1
cal = str(a)
if a < n:
    for i in range(1, n+1):
        print(str(i)+"!", "=", cal, "=", b)
        a += 1
        b *= (i+1)
        cal += "x" + str(a)



