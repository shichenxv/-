man=int(input("人数："))
step=int(input("步数："))
remainder=int(input("剩余人数："))
#获取用户输入
man = man + 1
shen=list(range(1,man))
#创建人数列表
while len(shen) > remainder:
    for i in range (1,step):
        a = shen[0]
        shen.remove(a)
        shen.append(a)
        #使列表旋转
    b = shen[0]
    shen.remove(b)
print(shen)#打印输出


