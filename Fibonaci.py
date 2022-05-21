ans = int(input("which number of fibonaci you want to know? : "))
a = 1
b = 1
i = 2
if ans in [1,2]:
    print(b)
elif ans%2 == 0:
    while i < ans:
        a += b
        b += a
        i += 2
    print(b)
else:
    while True:
        a = a+b
        i += 1
        if (i == ans):
            print( a)
        b += a
        i += 1
        
        
    
