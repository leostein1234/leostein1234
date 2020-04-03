def fibNum(num):
    new = 1
    old = 1
    for x in range(num - 1):
        temp = new
        new = old
        old = old + temp
    return new


print(fibNum(20))
