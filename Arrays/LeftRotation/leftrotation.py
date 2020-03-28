def rotLeft(a, d):
    return a[d:] + a[:d]

if __name__ == '__main__':
    n = 5
    d = 2
    a = [1,2,3,4,5]
    result = rotLeft(a,d)
    print(" ".join(str(x) for x in result))