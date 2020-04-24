from itertools import permutations, combinations,combinations_with_replacement
items=['a','b','c']
for p in permutations(items):
    print(p)
print(len(list(permutations(items))))

for p in permutations(items,2):
    print(p)

print('-'*20)
for c in combinations(items,3):
    print(c)

for c in combinations(items,2):
    print(c)

for c in combinations(items,1):
    print(c)

for c in combinations_with_replacement(items,3):
    print(c)