import random as rnd

kagen=2#
jogen=5#

f=open("test.bin","rb")
sum=[0]*93
a=[]
for i in range(93):
    aa=[]
    for j in range(93):
        b=f.read(2)
        aaa=b[0]*256+b[1]
        aa=aa+[aaa]
        sum[i]=sum[i]+aaa
    a=a+[aa]
f.close
#print(a)

c=[]
n=0#
front=0
while n<jogen:#
    r=rnd.randint(1+(n<kagen)*a[front][0],sum[front])#
    count=0
    i=-1
    while count<r:
        i=i+1
        count=count+a[front][i]
    #print(i)
    if i==0:
        break
    #c=c+[i+(227*256+130)*256+160+(i>32)*192]
    c=c+[227,130+(i>31),i+160-(i>31)*64]
    front=i
    n=n+1#
#print(c)
cc=bytes(c).decode("utf-8")
print(cc)