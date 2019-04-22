# Use "pass" to do nothing :-)

x = 0
while x < 8:
    x += 1
    if x == 4:
        pass
        # you need a block
        # here, so if you have
        # nothing to do,
        # type "pass"
    print(x)
