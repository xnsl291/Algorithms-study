total = int(input())
howMany = int(input())
price_sum = 0

for i in range(howMany):
    product = list(map(int,input().split()))
    price_sum+=product[0]*product[1]
print("Yes" if price_sum == total else "No")
