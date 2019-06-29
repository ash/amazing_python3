# Multiplying by 2 using shift

val = 10
val <<= 2 # mul by 4
print(val)

val = 1 
for _ in range(5):
    val <<= 1 # *= 2
    print(val)