import re # let's use regexes

s = "Count all CAPITAL letters "\
    "in the given String"

capitals = re.findall('([A-Z])', s)
# capitals will be a list. Each element
# contains only one letter

print(len(capitals)) # so the length
# of "capitals" is the number of capital
# letters 