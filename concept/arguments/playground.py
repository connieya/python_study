def add(*args):
    # 아스테리크스
    print(type(args))  # <class 'tuple'>
    res = 0
    for n in args:
        res += n
    return res


res = add(1, 2, 3, 4, 5, 6)
print(res)
