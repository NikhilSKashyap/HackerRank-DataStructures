#https://www.hackerrank.com/challenges/crush/forum/comments/505698

def arrayManipulation(n, queries):
    array = [0] * (n + 1)
    
    for query in queries: 
        a = query[0] - 1
        b = query[1]
        k = query[2]
        array[a] += k
        array[b] -= k
        
    max_value = 0
    running_count = 0
    for i in array:
        running_count += i
        if running_count > max_value:
            max_value = running_count
            
    return max_value

if __name__ == '__main__':
    n = 5
    queries = [[1,2,100],[2,5,100],[3,4,100]]
    print(arrayManipulation(n,queries))
