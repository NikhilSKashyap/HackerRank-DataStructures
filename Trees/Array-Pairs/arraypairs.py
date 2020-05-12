def solve(arr):
    a = []
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] * arr[j] <= max(arr[i:j + 1]):
                a.append(set([i + 1, j + 1]))
    return len(a)


if __name__ == '__main__':
    arr = [1, 1, 2, 4, 2]
    a = solve(arr)
    print(a)
