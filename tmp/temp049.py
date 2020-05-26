# 获取 100 以内的质数

num=[]
i=2
for i in range(2,100):
    j=2
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        num.append(i)
print(num)


# 方法2
import math
def func_get_prime(n):
    return filter(lambda x: not[x%i for i in range(2,int(math.sqrt(x)+1)) if x%i==0],range(2,n+1))
print(list(func_get_prime(100)))
for p in func_get_prime(100):
    print(p)
