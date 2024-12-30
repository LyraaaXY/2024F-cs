small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
big = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
k = int(input())
string = input()
result = []
while k > 26:
    k -= 26
for i in range(len(string)):
    for j in range(26):
        if string[i] == small[j]:
            num = j - k
            if num < 0:
                num += 26
            result.append(small[num])
        elif string[i] == big[j]:
            num = j - k
            if num < 0:
                num += 26
            result.append(big[num])
print(''.join(result))