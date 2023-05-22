while True:
    n=int(input())
    # 頂 底 東 西 南 北
    if n==0: break
    die=[1,6,4,3,5,2]
    while n!=0:
        n-=1
        pos=input()
        if pos == "north":
            temp=die[0]
            # 頂 -> 南
            die[0]=die[4]

            # 南 -> 底
            die[4]=die[1]

            # 底 -> 北
            die[1]=die[5]

            # 北 -> 頂
            die[5]=temp
        elif pos == "south":
            temp=die[0]
            #頂
            die[0]=die[5]

            # 北
            die[5]=die[1]

            # 底
            die[1]=die[4]

            # 南 
            die[4]=temp
        elif pos == "east":
            temp=die[0]
            # 頂
            die[0]=die[3]

            # 西
            die[3]=die[1]

            # 底 
            die[1]=die[2]

            # 東 
            die[2]=temp
        elif pos == "west":
            temp=die[0]
            # 頂
            die[0]=die[2]

            # 東
            die[2]=die[1]

            # 底 
            die[1]=die[3]

            # 西 
            die[3]=temp
    print(die[0])



    # while True:

    # num=int(input())
    # if num==0:
    #     break
    # dict={'top':1,'west':3,'north':2}
    # for i in range(num):

    # #    # 1 6 4 3 5 2
    # #    # 頂底東西南北
    #     temp=dict["top"]
    #     pos=input()
    #     if pos=='north':
    #         dict["top"]=7-dict["north"]
    #         dict["north"]=temp
    #     if pos=="south":
    #         dict["top"]=dict["north"]
    #         dict["north"]=7-temp
    #     if pos=="east":
    #         dict["top"]=dict["west"]
    #         dict["west"]=7-temp
    #     if pos=='west':
    #         dict["top"]=7-dict["west"]
    #         dict["west"]=temp
    # print(dict["top"])