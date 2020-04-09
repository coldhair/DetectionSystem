# 生成器函数
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

d=sample()
print(d)
for x in d:
    print(x)

text=''.join(sample())
print(text)