import csv
import itertools
from collections import Counter
import random
#with open('/Users/dmerrifield/Downloads/DKSalaries.csv', newline='') as csvfile:
#   reader = csv.reader(csvfile, delimiter=',')
#    for row in reader:
#        print(row)

headers = ['QB', 'RB', 'RB', 'WR', 'WR', 'WR', 'TE', 'FLEX', 'DST']

salaryLimit = 50000
salaryWaste = 400

qbPool = ['Aaron Rodgers','Josh Allen']
rbPool = ['Aaron Jones','Ronald Jones II','Clyde Edwards-Helaire']
wrPool = ['Davante Adams','Stefon Diggs','Tyreek Hill','Cole Beasley','Allen Lazard','John Brown','Mike Evans']
tePool = ['Robert Tonyan','Travis Kelce']
dstPool = ['Chiefs','Packers']
flexPool = rbPool + wrPool + tePool

coreStack = ['Davante Adams','Robert Tonyan','Stefon Diggs']
runBack = ['Cole Beasley','John Brown']

runBackLimit = 1

setExposure = False

exposure = ['Jaguars:20','Antonio Gibson:30']

#setPairs = True

#pairs = [

output = '/Users/dmerrifield/lineups_main_slate.csv'

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
                    player.append(Player(row[2], row[5], row[0], row[7], row[1]))
                    #print(player[count].name)
                count+=1

            self.details = list(csv_input)

    def get_col_row(self, col, row):
        return self.details[row-1][col-1]
    
class Player:
    def __init__(self, name, salary, position, team, id):
        self.name = name
        self.salary = salary
        self.position = position
        self.team = team
        self.id = id
        
    #def get_salary_by_name(self, name):
        #if self.name == name           
player = []

data = PlayerDetails('/Users/dmerrifield/Downloads/DKSalaries_main_slate.csv')

lineupCount = 10
qbPoolID = []
rbPoolID = []
wrPoolID = []
tePoolID = []
flexPoolID = []
dstPoolID = []

for x in range(len(qbPool)):
    for y in range(len(player)):
        if player[y].name == qbPool[x]:
            qbPoolID.append(y)
            
for x in range(len(rbPool)):
    for y in range(len(player)):
        if player[y].name == rbPool[x]:
            rbPoolID.append(y)
            
for x in range(len(wrPool)):
    for y in range(len(player)):
        if player[y].name == wrPool[x]:
            wrPoolID.append(y)
            
for x in range(len(tePool)):
    for y in range(len(player)):
        if player[y].name == tePool[x]:
            tePoolID.append(y)
            
for x in range(len(flexPool)):
    for y in range(len(player)):
        if player[y].name == flexPool[x]:
            flexPoolID.append(y)
            
for x in range(len(dstPool)):
    for y in range(len(player)):
        if player[y].name.strip() == dstPool[x]:
            dstPoolID.append(y)
            
print(qbPoolID)
print(rbPoolID)
print(wrPoolID)
print(tePoolID)
print(flexPoolID)
print(dstPoolID)

#for list in itertools.product(*playerPool):
#    print(list)
    
lineupCount=0
lineups=[]
lineupsID=[]

for qb in range(len(qbPool)):
    salaryTotal = 0
    for rb in range(len(rbPool)):
        for rb2 in range(len(rbPool)):
            if rbPool[rb] != rbPool[rb2]:
                for wr in range(len(wrPool)):
                    for wr2 in range(len(wrPool)):
                        if wrPool[wr] != wrPool[wr2]:
                            for wr3 in range(len(wrPool)):
                                if (wrPool[wr] != wrPool[wr3]) and (wrPool[wr2] != wrPool[wr3]):
                                    for te in range(len(tePool)):
                                        for flex in range(len(flexPool)):
                                            for dst in range(len(dstPool)):
                                                #print(qbPool[qb],rbPool[rb],rbPool[rb2],wrPool[wr],wrPool[wr2],wrPool[wr3],tePool[te], dstPool[dst])
                                                tmpLineupID = [qbPoolID[qb],rbPoolID[rb],rbPoolID[rb2],wrPoolID[wr],wrPoolID[wr2],wrPoolID[wr3],tePoolID[te], flexPoolID[flex], dstPoolID[dst]]
                                                tmpLineup = [qbPool[qb],rbPool[rb],rbPool[rb2],wrPool[wr],wrPool[wr2],wrPool[wr3],tePool[te], flexPool[flex], dstPool[dst]]
                                                
                                                #check for dupes
                                                if len(tmpLineup) == len(set(tmpLineup)):
                                                    #print(tmpLineup)
                                                    salaryTotal=0
                                                    for x in range(len(tmpLineup)):
                                                        salaryTotal = salaryTotal + int(player[tmpLineupID[x]].salary)
                                                    if (salaryTotal <= salaryLimit) and (salaryTotal > (salaryLimit - salaryWaste)):
                                                        #print(len(lineups))
                                                        lineups.append(tmpLineup)
                                                        lineupsID.append(tmpLineupID)                                 
                                                        lineupCount+=1
                                                        
                                                    
#for x in range(len(lineups)):
#    print(x)
#    print(lineups[x])
#    print(lineupsID[x])

seen = set()
uniqueLineups = []
uniqueLineupsID = []

for x in lineups:
    srtd = tuple(sorted(x))
    if srtd not in seen:
        uniqueLineups.append(x)
        seen.add(srtd)
        
for x in lineupsID:
    srtd = tuple(sorted(x))
    if srtd not in seen:
        uniqueLineupsID.append(x)
        seen.add(srtd)
 
tmpLineups = []
tmpLineupsID = []
for x in range(len(uniqueLineups)):
    if(set(coreStack).issubset(set(uniqueLineups[x]))):
        runBackCount = 0
        for y in range(len(runBack)):
            if(runBack[y] in uniqueLineups[x]):
                runBackCount+=1
        if (runBackCount <= runBackLimit) and (runBackCount >= 1):
            tmpLineups.append(uniqueLineups[x])
            tmpLineupsID.append(uniqueLineupsID[x])
    #for w in range uniqueLineups[x]:

uniqueLineups = tmpLineups
uniqueLineupsID = tmpLineupsID

random.shuffle(uniqueLineups)

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

    #uniqueLineups = tmpLineups
    #uniqueLineupsID = tmpLineupsID
    #for w in range uniqueLineups[x]:

    #uniqueLineups = tmpLineups
    #uniqueLineupsID = tmpLineupsID
        
#for x in range(len(tmpLineups)):
#    print(x)
#    print(tmpLineups[x])
    #print(uniqueLineupsID[x])
    
#for x in range(len(uniqueLineups)):
#    print(x)
#    print(uniqueLineups[x])
#    print(uniqueLineupsID[x])


#print('QB' + '\t' + 'RB' + '\t' + 'WR' + '\t' + 'TE' + '\t' + 'DST')

with open(output, 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(headers)
    for x in range(len(uniqueLineupsID)):
        tmpLineup=[]
        for y in uniqueLineupsID[x]:
            tmpLineup.append(player[y].id)
        print(tmpLineup) 
        wr.writerow(tmpLineup)

print('\ngenerated ' + str(len(uniqueLineupsID)) + ' unique lineups worth more than $' + str(salaryLimit - salaryWaste))