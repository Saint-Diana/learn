# 序列和索引
# 序列是一个用于存储多个值的连续空间。每个值都对应一个整数的编号，称为索引。
# 字符串、数组、列表都是序列
# 索引分为正向递增索引和反向递减索引
s = 'hello world'
for i in range(0, len(s)):
    print(s[i], end='\t')

print('\n')
for i in range(-len(s), 0):
    print(s[i], end='\t')

print('\n')
i = len(s) - 1
while i >= 0:
    print(s[i], end='\t')
    i -= 1


# 切片操作
s = 'HelloWorld'
s1 = s[0:5:2] # 索引从0开始，到5结束（不包含5），步长为2
print('\n' + s1)

# 逆序字符串
s2 = s[::-1] # 相当于s2 = s[-1:-11:-1]
print(s2)

# 序列的操作
print(s.count('o')) # 统计子序列在序列中出现的次数
print(s.index('e')) # 如果给的字符串找不到就会报错ValueError:substring not found.
print('llo' in s) # 子序列包含于序列
print('llo' not in s) # 子序列不包含于徐磊
print(len(s))
print(max(s))
print(min(s))