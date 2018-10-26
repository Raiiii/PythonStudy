# -*- coding: utf-8 -*- 
n1 = 255
n2 = 1000
print (hex(n1))
print (hex(n2))

#创建函数
import math

def quadratic(a, b, c):   					 #python用**表示指数
    s1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)    #注意括号细节，影响到运算顺序
    s2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)    #（2*a）忘记加括号导致找了很久bug
    return s1 , s2
   	
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
   print('测试失败')
else:
    print('测试成功')
    #成功