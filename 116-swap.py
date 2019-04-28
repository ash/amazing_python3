# Swapping the content
# of two variables

left = 'knife'
right = 'fork'

print(f'Before: {left}, {right}')

left, right = right, left

print(f'After: {left}, {right}')