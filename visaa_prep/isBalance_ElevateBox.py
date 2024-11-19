n = int(input())
arr = list(map(int, input().split()))
total_sum = sum(arr)
left_sum = 0
balance_array = []

for i in range(n):
    right_sum = total_sum - left_sum - arr[i]
    balance = abs(left_sum - right_sum)
    balance_array.append(balance)
    left_sum += arr[i]

print(" ".join(map(str, balance_array)))
