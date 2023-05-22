t=int(input())
for i in range(t):
    b1=0
    b2=0
    n=int(input())
    n_bin=bin(n)[2:]
    for j in range(len(n_bin)):
        if n_bin[j]=='1':
            b1+=1
    n_dec=int(str(n),16)
    n_bin2=bin(n_dec)[2:]
    for k in range(len(n_bin2)):
        if n_bin2[k]=='1':
            b2+=1
    print(f"{b1} {b2}")