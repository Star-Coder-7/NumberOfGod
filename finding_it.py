from decimal import *

max_length = 23

goodSequence = [Decimal(0)] * (max_length + 1)

riskySequence = [Decimal(0)] * (max_length + 1)

total = [Decimal(0)] * (max_length + 1)

sum = [Decimal(0)] * (max_length + 1)

goodSequence[0], goodSequence[1] = Decimal(1), Decimal(18)
total[0], total[1] = Decimal(1), Decimal(18)
sum[0], sum[1] = Decimal(1), Decimal(18)

for x in range(2, max_length + 1):
    goodSequence[x] = goodSequence[x - 1] * 12 + riskySequence[x - 1] * 12
    riskySequence[x] = riskySequence[x - 1] * 3 / 2
    total[x] = goodSequence[x] + riskySequence[x]
    sum[x] = sum[x - 1] + total[x]

for x, num in enumerate(sum):
    enough = "not enough"
    if num >= Decimal(43252003274489856000):
        enough = "enough"
    print(str(x) + ": " + str(num) + " " + enough)
    if enough == "enough":
        pass
