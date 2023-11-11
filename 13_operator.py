# 逻辑运算符
# and
# or
# not
a, b = 3, 5
if(a > b and a + b > 0):
    print('x')

if(a > b or a + b > 0):
    print('y')

if(not a > b):
    print('z');

flag = False
if(not flag):
    print('flag == False')

def add(a:int, b:int) :
    return a + b;

print(add(5, 10))