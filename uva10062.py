while True:
    try:
        n=input()
        dic={}
        for i in n:
            if ord(i) not in dic.keys():
                dic[ord(i)]=1
            else:
                dic[ord(i)]+=1
        for k, v in sorted(dic.items(), key = lambda x:(x[1], -x[0])):
            print(k, v)
    except EOFError:
        break