import os

size = os.get_terminal_size().columns
print(size)
# 这东西只有在命令行玩的时候才有效
