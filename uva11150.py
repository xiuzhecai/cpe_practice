while True:
    try:
        n=int(input())
        cola=n
        while n>=3:
            cola+=n//3
            n=n//3+n%3
        if n==2:
            cola+=1
        print(cola)
    except EOFError:
        break