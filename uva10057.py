# while True:
#     try:
#         n=int(input())
#         dream=[]
#         for i in range(n):
#             num=int(input())
#             dream.append(num)
#         dream.sort()
#         dreamlen=len(dream)
#         index=(dreamlen-1)//2
    
#         mid=dream[index]
        
#         if n%2==0:
#             if dream[index]==dream[index+1]:
#                 fre=dream.count(mid)
#             else:
#                 fre=dream.count(mid)+dream.count(dream[index+1])
#         else:
#             fre=dream.count(mid)

        
#         if(n%2==1):numofmin=1
#         elif(dream[index+1]==dream[index]):numofmin=1
#         else:numofmin=dream[index+1]-mid

#         print(f"{mid} {fre} {numofmin}")
#     except EOFError:
#         break
while True:
    try:
        n = int(input())
        dream = []
        for i in range(n):
            dream.append(int(input()))
        dream.sort()
        lens = len(dream)
        ans2=0
        if lens%2 != 0:
            ans1=dream[lens//2]
            ans3=1
            for i in dream:
                if i==dream[lens//2]:
                    ans2+=1
        else:
            ans1=dream[lens//2-1]
            ans3=dream[lens//2]-dream[lens//2-1]+1
            for i in dream:
                if i==dream[lens//2] or i==dream[lens//2-1]:
                    ans2+=1
        print("{} {} {}".format(ans1,ans2,ans3))
    except EOFError:
        break