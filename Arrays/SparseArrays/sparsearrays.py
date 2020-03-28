def matchingStrings(strings, queries):
    arr=[]
    for item in queries:
        arr.append(strings.count(item))
    return arr

if __name__ == '__main__':
    n = 4
    strings = ["aba","baba","aba","xzxb"]
    q = 3
    queries = ["aba","xzxb","ab"]
    print(matchingStrings(strings,queries))