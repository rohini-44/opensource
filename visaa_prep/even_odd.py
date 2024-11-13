def check_winner(N):
    digit_sum = sum(int(digit) for digit in N)
    if digit_sum%2==0:
        return "Vignesh"
    else:
        return "Charan"
N = input().strip()
print(check_winner(N))
