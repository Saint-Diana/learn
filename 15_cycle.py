# 循环结构

# 遍历字符串
for i in 'hello':
    print(i)

arr = [1, 2, 3, 4, 5, 6]
for i in arr:
    print(i)

# range()用于产生一个[n, m)的整数序列
print('--------------------')
for i in range(3, 5):
    print(i)

# 所以如果想要和Java中一样，通过下标来遍历数组，就需要用到range()和len()
for i in range(0, len(arr)):
    print('arr[', i, '] = ', arr[i])

# 找100到999之间的水仙花数 154  ==> i % 10 = 4; i // 100 = 1
for i in range(100, 1000):
    if((i % 10) ** 3 + (i // 100) ** 3 + (i // 10 - i // 100 * 10) ** 3 == i):
        print(i, '为水仙花数')

# python特有的while...else...结构
num = 12345678
while num > 0:
    i = num % 10
    num //= 10
    print(i)

# 求1~100的累加和
ans = 0
cnt = 100
while cnt > 0:
    ans += cnt
    cnt -= 1
else: # 当不满足循环条件的情况下执行下面的代码
    print('ans =', ans)

# break和continue
def isPrime(n : int) -> bool:
    if(n <= 1):
        return False
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True;

for i in range(1, 101):
    if(isPrime(i)):
        print(i, '是素数')

# python独有的空语句pass，用于显示误操作的分支
# 例如
age = 17
if age < 18:
    pass
else:
    print('你成年了！')