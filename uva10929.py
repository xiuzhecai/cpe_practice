while True:
    n=input()
    if n=='0':
        break
    even=0
    odd=0
    for i in range(0,len(n),2):
        even += ord(n[i]) - 48
    for i in range(1,len(n),2):
        odd += ord(n[i]) - 48
    gap=abs(odd-even)
    if gap%11==0:
        print(f"{n} is a multiple of 11.")
    else:
        print(f"{n} is not a multiple of 11.")