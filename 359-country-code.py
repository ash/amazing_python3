from pycountry import countries

print(countries.get(alpha_2='DE').name)
print(countries.get(name='Germany').alpha_2)