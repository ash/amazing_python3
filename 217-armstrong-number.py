# Is the number an Armstrong number?
# Example: 153 is.
# 153 = 1^3 + 5^3 + 3^3
# 3 is the length of the number

def is_armstrong(n):
    pwr = len(str(n))
    s = sum(
        [int(x) ** pwr for 
         x in str(n)]
    )
    return s == n

print(is_armstrong(153)) # Yes
print(is_armstrong(154)) # No
print(is_armstrong(1634)) # Yes