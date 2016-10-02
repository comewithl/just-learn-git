import math
while 1:
    r=int(raw_input())
    k=math.sqrt(r)
    if int(k)==k:
        num=4
    else:
        num=0
    k=int(k)
    for i in range(1,k):
        if math.sqrt(r-i**2)==int(math.sqrt(r-i**2)):
            num=num+4
    print num