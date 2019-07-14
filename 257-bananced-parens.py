# Check if the parentheses are balanced
e = [
    '()', '((', '(Hello, (World))',
    ')Hello(', 'Right)', 'Le()ft'
]

def is_balanced(str):
    count = 0
    for ch in str:
        if ch == '(':
            count += 1
        elif ch == ')':
            count -= 1
        if count < 0:
            return False # first goes ')'
    return count == 0 # balanced

for s in e:
    print(s, is_balanced(s))