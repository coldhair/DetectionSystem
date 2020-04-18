mylist = [1, 4, -5, 10, -7, 2, 3, -1]
larger = [n for n in mylist if n > 0]
smaller = [n for n in mylist if n < 0]
print(larger)
print(smaller)
pos = (n for n in mylist if n > 0)
print(pos)
# print(list(pos))
print(next(pos))
print('-' * 8)
for x in pos:
    print(x)

vales = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, vales))
print(ivals)
clip_neg = [n if n > 0 else 0 for n in mylist ]
print(clip_neg)
