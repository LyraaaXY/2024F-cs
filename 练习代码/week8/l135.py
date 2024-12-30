kids = list(map(int, input().split()))
candies = [1]*(len(kids))
for i in range(1, len(kids)):
    if kids[i] > kids[i - 1]:
        candies[i] = candies[i - 1] + 1
    elif kids[i] < kids[i - 1] and candies[i - 1] == 1:
        candies[i - 1] += 1
print(sum(candies))