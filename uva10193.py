import math
n=int(input())
for i in range(n):
    s1=input()
    s2=input()
    dec=int(s1,2)
    dec2=int(s2,2)
    # x=2
    # coprime=1
    # while dec>=x and dec2>=x:
    #     if dec%x==0 and dec2%x==0:
    #         coprime=0
    #         break
    #     else:
    #         x+=1
    coprime=0
    
    x=math.gcd(dec,dec2)
    if x==1:
        coprime=1

    if coprime==0:
        print(f"Pair #{i+1}: All you need is love! ") 
    else:
        print(f"Pair #{i+1}: Love is not all you need!")