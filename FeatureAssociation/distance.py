# open outputBanksOutput.txt
import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


output = open('output.txt', 'w')
banks = open('outputBanksOutput.txt', 'r').readlines()
for bank in banks:
    latb = float(bank.split(' ')[0])
    longb = float(bank.split(' ')[1])
    for temp in banks:
        minArray = []
        lat = float(temp.split(' ')[0])
        long = float(temp.split(' ')[1])
        minArray.append(distance(latb, longb, lat, long))
    if (min(minArray)*100 < .5):
        output.write(bank.split(' ')[2])

output.close()
