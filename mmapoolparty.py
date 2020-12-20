#Dan Merrifield

import csv
import itertools
from collections import Counter
#import random

salaryLimit = 50000
salaryWaste = 300

allowOpponents = False
setExposure = False

headers = ['F', 'F', 'F', 'F', 'F', 'F']

flexPool = ['Stephen Thompson','Jose Aldo','Khaos Williams','Michel Pereira','Marlon Moraes','Marcin Tybura','Gillian Robertson','Jimmy Flick','Tafon Nchukwi']

exposure = ['Charles Oliveira:50']

output = '/Users/dmerrifield/lineups_mma.csv'

class PlayerDetails():
    def __init__(self, filename):
        with open(filename, "r") as f_input:
            csv_input = csv.reader(f_input)
            count = 0
            #player = []
            
            for row in csv_input:
                if count > 0:
                    print("loaded rows: " + str(count))
                    #print(row)
                    player.append(Player(row[2], row[5], row[0], row[6], row[1], row[4]))
                    #print(player[count].name)
                count+=1

            self.details = list(csv_input)

    def get_col_row(self, col, row):
        return self.details[row-1][col-1]
    
class Player:
    def __init__(self, name, salary, position, gameInfo, id, type):
        self.name = name
        self.salary = salary
        self.position = position
        self.gameInfo = gameInfo
        self.id = id
        self.type = type
        
    #def get_salary_by_name(self, name):
        #if self.name == name

player = []

data = PlayerDetails('/Users/dmerrifield/Downloads/DKSalaries_mma.csv')

lineupCount = 10

flexPoolID = []

for x in range(len(flexPool)):
    for y in range(len(player)):
        if (player[y].name.strip() == flexPool[x]):
            flexPoolID.append(y)           
            
print(flexPool)
print(flexPoolID)

#print('FLEX' + '\t' + 'FLEX' + '\t' + 'FLEX' + '\t' + 'FLEX' + '\t' + 'FLEX'+ '\t' + 'FLEX')
    
lineupCount=0
lineups=[]
lineupsID=[]

salary=[]

for flex in range(len(flexPool)):
    for flex2 in range(len(flexPool)):
        if flexPool[flex] != flexPool[flex2]:
            for flex3 in range(len(flexPool)):
                if (flexPool[flex] != flexPool[flex3]) and (flexPool[flex2] != flexPool[flex3]):
                    for flex4 in range(len(flexPool)):
                        if (flexPool[flex] != flexPool[flex4]) and (flexPool[flex2] != flexPool[flex4]) and (flexPool[flex3] != flexPool[flex4]):
                            for flex5 in range(len(flexPool)):
                                if (flexPool[flex] != flexPool[flex5]) and (flexPool[flex2] != flexPool[flex5]) and (flexPool[flex3] != flexPool[flex5]) and (flexPool[flex4] != flexPool[flex5]):
                                     for flex6 in range(len(flexPool)):
                                        if (flexPool[flex] != flexPool[flex6]) and (flexPool[flex2] != flexPool[flex6]) and (flexPool[flex3] != flexPool[flex6]) and (flexPool[flex4] != flexPool[flex6]) and (flexPool[flex5] != flexPool[flex6]):

                                            tmpLineupID = [flexPoolID[flex],flexPoolID[flex2],flexPoolID[flex3],flexPoolID[flex4],flexPoolID[flex5],flexPoolID[flex6]]
                                            tmpLineup = [flexPool[flex],flexPool[flex2],flexPool[flex3],flexPool[flex4],flexPool[flex5],flexPool[flex6]]
                                            
                                            #print(tmpFlex)
                                            
                                            #check for dupes
                                            if len(tmpLineup) == len(set(tmpLineup)):
                                                #print(tmpLineup)
                                                salaryTotal=0
                                                for x in range(len(tmpLineup)):
                                                    salaryTotal = salaryTotal + int(player[tmpLineupID[x]].salary)
                                                if (salaryTotal <= salaryLimit) and (salaryTotal > (salaryLimit - salaryWaste)):
                                                    #print(len(lineups))
                                                    #print(lineupCount)
                                                    lineups.append(tmpLineup)
                                                    lineupsID.append(tmpLineupID)
                                                    salary.append(salaryTotal)
                                                    lineupCount+=1
                                                        
                                                    
#for x in range(len(lineups)):
#    print(x)
#    print(lineups[x])
#    print(lineupsID[x])

seen = set()
uniqueLineups = []
uniqueLineupsID = []

#for x in flexLineups:
#    srtd = tuple(sorted(x))
#    if srtd not in seen:
#       uniqueFlexLineups.append(x)
#        seen.add(srtd)
        
for x in lineupsID:
    srtd = tuple(sorted(x))
    if srtd not in seen:
        uniqueLineupsID.append(x)
        seen.add(srtd)
        
for x in lineups:
    srtd = tuple(sorted(x))
    if srtd not in seen:
        uniqueLineups.append(x)
        seen.add(srtd)

tmpUniqueLineupsID = []
tmpUniqueLineups= []

if allowOpponents == False:
    for x in range(len(uniqueLineupsID)):
        #print(x)
        #print(uniqueLineups[x])
        #print(uniqueLineupsID[x])
        oppCheck = False
        #print('LINEUP ' + str(x))
        for y in uniqueLineupsID[x]:
            #print(player[y].id)
            for z in uniqueLineupsID[x]:
                if y != z:
                    #print(player[y].gameInfo + ' ' + player[z].gameInfo)
                    if player[y].gameInfo == player[z].gameInfo:
                        oppCheck = True
        #print('LINEUP ' + str(x) + ' ' + str(oppCheck))
        if oppCheck == False:
            tmpUniqueLineupsID.append(uniqueLineupsID[x])
            tmpUniqueLineups.append(uniqueLineups[x])

    uniqueLineupsID = tmpUniqueLineupsID
    uniqueLineups = tmpUniqueLineups


if setExposure:
    
    print("Checking exposure")
    
    tmpLineups = []
    tmpLineupsID = []
    
    # for now just determine if the lineups do not contain any player in our exposure pool.
    #This allows us to accurately determine how many lineups of each participant will be allowed after pruning. 
    
    for x in range(len(uniqueLineupsID)):

        validLineup = True

        for y in range(len(exposure)):

            exposureCount = 0
            playerName = exposure[y].split(':')[0]
            playerExposure = float(int(exposure[y].split(':')[1]) / 100)
            #print(playerName + ' with exposure ' + str(playerExposure * 100) + '%\n')
            
            if playerName in uniqueLineups[x]:
                validLineup = False
        
        if validLineup:
            #print("Valid lineup found " + str(uniqueLineups[x]))
            tmpLineups.append(uniqueLineups[x])
            tmpLineupsID.append(uniqueLineupsID[x])
    
    #shuffledLineups = uniqueLineups
    
    baseLength = len(tmpLineups)
    
    print(str(baseLength) + " lineups without exposure-checked players")
    
    for x in range(len(exposure)):
        exposureCount = 0
        for y in range(len(uniqueLineupsID)):
            playerName = exposure[x].split(':')[0]
            playerExposure = float(int(exposure[x].split(':')[1]) / 100)
            
            #print("player " + playerName + " with exposure of " + str(playerExposure))
            
            if playerName in uniqueLineups[y] and exposureCount <= (baseLength * playerExposure) and uniqueLineups[y] not in tmpLineups:
                print('exposureCount for ' + playerName + ' equal to ' + str(exposureCount) + ' out of ' + str(baseLength * playerExposure))
                tmpLineups.append(uniqueLineups[y])
                tmpLineupsID.append(uniqueLineupsID[y])
                exposureCount+=1
                baseLength+=1
                
            
    uniqueLineups = tmpLineups
    uniqueLineupsID = tmpLineupsID


        
with open(output, 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(headers)
    for x in range(len(uniqueLineupsID)):
        tmpLineup=[]
        for y in uniqueLineupsID[x]:
            tmpLineup.append(player[y].id)
        print(tmpLineup) 
        wr.writerow(tmpLineup)
        
if allowOpponents:
    print('\ngenerated ' + str(len(uniqueLineupsID)) + ' unique lineups worth more than $' + str(salaryLimit - salaryWaste) + ' with opponents ALLOWED')
else:
    print('\ngenerated ' + str(len(uniqueLineupsID)) + ' unique lineups worth more than $' + str(salaryLimit - salaryWaste) + ' with opponents NOT ALLOWED')
   