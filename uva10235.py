while True:
    try:
        n=int(input())
        n1=n
        nre=0
        prime=0
        coprime=0
        emirp=0
        while n1!=0:
            nre=nre*10+n1%10
            n1=n1//10

        for i in range(2,n):
            if n%i==0:
                coprime=1
                print(f"{n} is not prime.")
                break
        for i in range(2,n):
            if n%i!=0 and nre%i!=0 and n!=nre:
                emirp=1
            else:
                prime=1
        if coprime==0 and emirp==1 and prime==0:
            print(f"{n} is emirp.")
        if coprime ==0 and prime==1:
            print(f"{n} is prime.")
    except EOFError:
        break