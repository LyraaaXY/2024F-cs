import heapq

def max_potions(n, potions):
    health = 0
    consumed = []
    for potion in potions:
        health += potion
        heapq.heappush(consumed, potion)
        if health < 0:
            if consumed:
                health -= consumed[0]
                heapq.heappop(consumed)
    return len(consumed)

n = int(input())
potions = list(map(int, input().split()))
print(max_potions(n, potions))