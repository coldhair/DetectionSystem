def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

#这个方法仅仅在序列中元素为 hashable 的时候才管用。

if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(dedupe(a))
    print(list(dedupe(a)))
    for x in dedupe(a):
        print(x)
    # 如果不关心顺序，可以直接构造集合来实现,如下
    print(list(set(a)))