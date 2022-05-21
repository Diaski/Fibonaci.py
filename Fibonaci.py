a = 1;b = 1;i = 2
ans = int(input("which number of fibonaci you want to know? : "))
while i < ans:
        a+=b
        b+=a
        i+=2
if (ans%2 == 0):
    print(b)
else:
    print(a)
