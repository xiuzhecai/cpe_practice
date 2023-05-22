
num=int(input())
for i in range(num):
    num,pos_str= input().split(' ',1)
    num=int(num)
    poslen=int(num)
    pos=list(map(int,pos_str.split(' ')))
    for i in range(num):
        pos[i]=int(pos[i])
    pos.sort()
    index=(poslen-1)//2
    if(poslen%2==0):
        mid=(pos[index]+pos[index+1])//2
    else:   
        mid=pos[index]
    distance=0
    for i in range(len(pos)):
        distance=distance+abs(pos[i]-mid)
    print(distance)


# input_nums = int(input())
# for i in range(input_nums):
#     house_num_str, house_pos_str = input().split(' ',1)

#     poslen = int(house_num_str)
#     house_pos = list( map(int, house_pos_str.split(' ')) )
#     house_pos.sort()

#     index=(poslen-1)//2

#     if(poslen%2==0):
#         mid = ( house_pos[index]+ house_pos[index+1] ) // 2
#     else:
#         mid = house_pos[index]

#     distance=0
#     for i in range(poslen):
#         distance = distance + abs(house_pos[i]- mid)
#     print(distance)