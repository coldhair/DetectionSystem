def some_func():
    try:
        return 'from_try'
    finally:
        return 'from_finally'

some_func()
print(some_func())

for i in range(4):
    print(i)
    i=10

row=['']*3
board=[row]*3
print(board)