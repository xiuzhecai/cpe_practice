n=int(input())
for i in range(n):
    a=int(input())
    b=int(input())
    sum=0
    for k in range(b-a+1):
        if(a%2==1):
            sum+=a
        a+=1
    print(f"Case {i+1}: {sum}") 