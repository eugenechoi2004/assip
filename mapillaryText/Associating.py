# read in a csv file FinalLogo.csv
'''
divide the section up into blocks
And see which images fall into the blocks

'''

import pandas as pd

logos = pd.read_csv(
    '/Users/eugene/Documents/GitHub/assip/mapillaryText/FinalLogos.csv')

# read in the outputBanks.txt file

banks = open('outputBanks.txt', 'r').readlines()
newFile = open('outputBanksOutput.txt', 'w')
for bank in banks:
    latb = float(bank.split(' ')[0])
    longb = float(bank.split(' ')[1])
    for i in range(len(logos['Lat'])):
        lat = float(logos['Lat'][i])
        long = float(logos['Long'][i])
        if latb == lat and longb == long:
            newFile.write(str(lat)+' '+str(long)+' ' +
                          str(logos['ImageId'][i])+'\n')
            break
newFile.close()
