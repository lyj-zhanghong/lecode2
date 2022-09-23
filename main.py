s = input()
n = len(s)
start = 0;end = 0;lengths=0;result=0
for end in range(n):
    tempChar = s[end]
    index = start
    for index in range(end):
        if tempChar == s[index]:
            start = index+1
            lengths = end-start
            break
    lengths = lengths+1
    result = max(result,lengths);
print(result)