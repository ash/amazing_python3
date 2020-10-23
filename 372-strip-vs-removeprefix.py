# The difference between "strip"
# and "removeprefix"

word = 'afterparty'

print(word.strip('after'))
print(word.removeprefix('after'))
# you get "party" and "party"

print(word.strip('afterp'))
print(word.removeprefix('afterp'))
# you get "y" and "arty"
