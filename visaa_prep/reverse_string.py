def reverse(n):
    neg = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0

    while n != 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    
    reversed_num *= neg
    
    if reversed_num < -2147483648 or reversed_num > 2147483647:
        return 0
    return reversed_num

n = int(input())
print(reverse(n))
