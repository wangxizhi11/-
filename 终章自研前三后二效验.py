print("\033[1;34;40m终章出品必属精品\033[0m")
qq=int(input("请输入QQ(1有,2没有):"))
ks=int(input("请输入ks名字(1有,2没有)"))

q3=int(input('请输入手机号的前三位(已知手机号-1如111就输入110):'))
q2=int(input("请输入手机号的手机号的后两位："))
q6=1000000
q1=0
while q1<834930:
    q6=q6+1
    n=(q3*100000000+q6*100+q2)
    if n==17783493042:
        print(str(n)+"\033[1;34;40m效验成功\033[0m")
    else:
        print(str(n)+"\033[1;31;40m效验失败\033[0m")
        q1+=1
        
    
    
import time



print("Loading",end = "")
for i in range(20):
    print(".",end = '',flush = True)
    time.sleep(0.5)

