S = input()
res = 0
string = 1
for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        string += 1
    else:
        res = max(res, string)
        string = 1
res = max(res, string)
print(res)