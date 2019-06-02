# Handling the German letter ß
# (which is equivalent to "ss")

str1 = 'strasse'
str2 = 'straße' # street in English

print(str1 == str2) # False

print(
    str1.casefold() ==
    str2.casefold()
) # True
