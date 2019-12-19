# Check if the phrases are anagrams

from collections import Counter

str1 = "rail safety"
str2 = "fairy tales"
str3 = "fairy tail"

print(Counter(str1) == Counter(str2))
print(Counter(str1) == Counter(str3))
