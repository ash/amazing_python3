# Count letters in the given text.
# Print the stats in descending order.

message = 'Hello, World!'
stats = { # dictionary comprehension
    letter: message.count(letter)
        for letter in message
}

for x in sorted(
    # sort by value, descending order
    stats, key=stats.get, reverse=True):
    print(f'{x} = {stats[x]}')
