n=int(input())
dic={}
for i in range(n):
    cryptanalysis=input()
    for c in cryptanalysis:
        c=c.upper()
        if not c.isalpha():
            continue
        if c not in dic.keys():
            dic[c]=1
        else:
            dic[c]+=1
for a,b in sorted(dic.items(),key=lambda x:(-x[-1],x[0])):
    print(a,b)

#這太難了
