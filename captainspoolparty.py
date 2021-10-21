#Dan Merrifield

import csv
import itertools
from collections import Counter

salaryLimit = 50000
salaryWaste = 400

setExposure = True
setAvoidPairs = True
setQBCount = True

qbMin = 1
qbMax = 2

headers = ['CPT', 'FLEX', 'FLEX', 'FLEX', 'FLEX', 'FLEX']

cptPool = ['Noah Fant','Jarvis Landry','D\'Ernest Johnson','Case Keenum']
flexPool = ['Noah Fant','Jarvis Landry','D\'Ernest Johnson','Case Keenum','Jarvis Landry','Teddy Bridgewater','Courtland Sutton','Tim Patrick','Javonte Williams','Donovan Peoples-Jones','Austin Hooper','Rashard Higgins','Demetric Felton','Brandon McManus','Chase McLaughlin']

#exposure = ['DeVonta Smith:30']
exposure = ['Courtland Sutton:40']

#avoidPairs = ['Mike Evans:Chris Godwin']
avoidPairs = ['Demetric Felton:D\'Ernest Johnson','Jarvis Landry:Donovan Peoples-Jones','Courtland Sutton:Tim Patrick']

output = '/Users/dmerrifield/lineups_captain.csv'

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
                    player.append(Player(row[2], row[5], row[0], row[7], row[1], row[4]))
                    #print(player[count].name)
                count+=1
                
            print()    
            self.details = list(csv_input)

    def get_col_row(self, col, row):
        return self.details[row-1][col-1]
    
class Player:
    def __init__(self, name, salary, position, team, id, type):
        self.name = name
        self.salary = salary
        self.position = position
        self.team = team
        self.id = id
        self.type = type
        
    #def get_salary_by_name(self, name):
        #if self.name == name

player = []

data = PlayerDetails('/Users/dmerrifield/Downloads/DKSalaries_captains.csv')

lineupCount = 10
cptPoolID = []
flexPoolID = []

for x in range(len(cptPool)):
    for y in range(len(player)):
        if (player[y].name.strip() == cptPool[x]) and (player[y].type == 'CPT'):
            cptPoolID.append(y)
            
for x in range(len(flexPool)):
    for y in range(len(player)):
        if (player[y].name.strip() == flexPool[x]) and (player[y].type == 'FLEX'):
            flexPoolID.append(y)           
            
print(cptPoolID)
print(flexPoolID)

#print('CPT' + '\t' + 'FLEX' + '\t' + 'FLEX' + '\t' + 'FLEX' + '\t' + 'FLEX'+ '\t' + 'FLEX')
    
lineupCount=0
lineups=[]
lineupsID=[]

flexLineupID=[]
flexLineup=[]

salary=[]

for cpt in range(len(cptPool)):
    salaryTotal = 0
    for flex in range(len(flexPool)):
        for flex2 in range(len(flexPool)):
            if flexPool[flex] != flexPool[flex2]:
                for flex3 in range(len(flexPool)):
                    if (flexPool[flex] != flexPool[flex3]) and (flexPool[flex2] != flexPool[flex3]):
                        for flex4 in range(len(flexPool)):
                            if (flexPool[flex] != flexPool[flex4]) and (flexPool[flex2] != flexPool[flex4]) and (flexPool[flex3] != flexPool[flex4]):
                                for flex5 in range(len(flexPool)):
                                    if (flexPool[flex] != flexPool[flex5]) and (flexPool[flex2] != flexPool[flex5]) and (flexPool[flex3] != flexPool[flex5]) and (flexPool[flex4] != flexPool[flex5]):

                                        tmpLineupID = [cptPoolID[cpt],flexPoolID[flex],flexPoolID[flex2],flexPoolID[flex3],flexPoolID[flex4],flexPoolID[flex5]]
                                        tmpLineup = [cptPool[cpt],flexPool[flex],flexPool[flex2],flexPool[flex3],flexPool[flex4],flexPool[flex5]]
                                        
                                        tmpFlexLineupID = [flexPoolID[flex],flexPoolID[flex2],flexPoolID[flex3],flexPoolID[flex4],flexPoolID[flex5]]
                                        tmpFlexLineup = [flexPool[flex],flexPool[flex2],flexPool[flex3],flexPool[flex4],flexPool[flex5]]
                                        
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
                                                #print(tmpLineup)
                                                #print(salaryTotal)
                                                lineups.append(tmpLineup)
                                                flexLineup.append(tmpFlexLineup)
                                                lineupsID.append(tmpLineupID)
                                                flexLineupID.append(tmpFlexLineupID)
                                                salary.append(salaryTotal)
                                                lineupCount+=1
                                                        
                                                    
#for x in range(len(lineups)):
#    print(x)
#    print(lineups[x])
#    print(lineupsID[x])

seen = set()
uniqueLineups = []
uniqueLineupsID = []
uniqueFlexLineups = []
uniqueFlexLineupsID = []

#for x in flexLineups:
#    srtd = tuple(sorted(x))
#    if srtd not in seen:
#       uniqueFlexLineups.append(x)
#        seen.add(srtd)
        
count=0
for x in lineupsID:
    srtd = tuple(sorted(x))
    if srtd not in seen:
        uniqueLineupsID.append(x)
        uniqueLineups.append(lineups[count])
        seen.add(srtd)
    count+=1
        
#for x in lineups:
#    srtd = tuple(sorted(x))
#    if srtd not in seen:
#        uniqueLineups.append(x)
#        seen.add(srtd)

#for x in range(len(uniqueLineupsID)):
    #print(x)
    #print(uniqueLineups[x])
    #print(uniqueLineupsID[x])
    #for y in uniqueLineupsID[x]:
        #print(player[y].id)        

#optimizer

if setAvoidPairs:
    
    print("\nChecking for avoided pairs")
    
    tmpLineups = []
    tmpLineupsID = []
    
    for x in range(len(avoidPairs)):
        avoidA = avoidPairs[x].split(':')[0]
        avoidB = avoidPairs[x].split(':')[1]
        for y in range(len(uniqueLineupsID)):    
            if avoidA not in uniqueLineups[y] or avoidB not in uniqueLineups[y]:
                tmpLineups.append(uniqueLineups[y])
                tmpLineupsID.append(uniqueLineupsID[y])
    
        uniqueLineups = tmpLineups
        uniqueLineupsID = tmpLineupsID
        tmpLineups = []
        tmpLineupsID = []
 

if setQBCount:
    
    print("\nChecking QB count settings")
    
    tmpLineups = []
    tmpLineupsID = []
    
    for x in range(len(uniqueLineupsID)):
        
        qbCount = 0
        
        for y in range(len(uniqueLineupsID[x])):
            if player[uniqueLineupsID[x][y]].position == 'QB':
                qbCount+=1
        
        if qbCount >= qbMin and qbCount <= qbMax : 
            tmpLineups.append(uniqueLineups[x])
            tmpLineupsID.append(uniqueLineupsID[x])
    
    uniqueLineups = tmpLineups
    uniqueLineupsID = tmpLineupsID
        
        
#exposure

if setExposure:
    
    print("\nChecking exposure")
    print(len(uniqueLineups))
    print(len(uniqueLineupsID))
    
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

print()
with open(output, 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(headers)
    for x in range(len(uniqueLineupsID)):
        tmpLineup=[]
        for y in uniqueLineupsID[x]:
            tmpLineup.append(player[y].id)
        print(tmpLineup) 
        wr.writerow(tmpLineup)

#print total exposure for all players
print("\nCPT DISTRIBUTION:")
for x in range(len(cptPool)):
    count = 0
    for y in range(len(uniqueLineups)):
        if cptPool[x] == uniqueLineups[y][0]:
            count+=1
    print('CPT  ' + cptPool[x] + ':  ' + str(count))  

print("\nFLEX DISTRIBUTION:")
for x in range(len(flexPool)):
    count = 0
    for y in range(len(uniqueLineups)):
        if flexPool[x] in uniqueLineups[y] and uniqueLineups[y].index(flexPool[x]) != 0:
            count+=1
    print('FLEX ' + flexPool[x] + ':  ' + str(count))  


print('\ngenerated ' + str(len(uniqueLineupsID)) + ' unique lineups worth more than $' + str(salaryLimit - salaryWaste))
