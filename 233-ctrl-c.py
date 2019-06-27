# Catching "Ctrl+C"

c = 0 # counter

try:
    while 1: # infinite loop
        c += 1
except KeyboardInterrupt:
    print(f'The counter is {c} now')
