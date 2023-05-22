while True:
    n=input()
    a,b=n.split(' ',1)
    if len(a)>len(b):
        x=len(a)
    else:
        x=len(b)
    a=int(a)
    b=int(b)
    if a==0 and b==0:
        break
    y=0
    ca=0
    for i in range(x):
        c=a%10
        d=b%10
        if c+d+ca>=10:
            y+=1
            ca=1
        else:ca=0
        a=a//10
        b=b//10
    if y==0:
        print("No carry operation.")
    elif y==1:
        print("1 carry operation.")
    else:
        print(f"{y} carry operations.")
