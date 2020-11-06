import csv
import itertools
from collections import Counter
#with open('/Users/dmerrifield/Downloads/DKSalaries.csv', newline='') as csvfile:
#   reader = csv.reader(csvfile, delimiter=',')
#    for row in reader:
#        print(row)

salaryLimit = 50000
salaryWaste = 400

runBackLimit = 1

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

data = PlayerDetails('/Users/dmerrifield/Downloads/DKSalaries.csv')

qbPool = ['Ryan Tannehill']
rbPool = ['Alvin Kamara', 'La\'Mical Perine', 'Jonathan Taylor', 'Kareem Hunt', 'Myles Gaskin', 'James White']
wrPool = ['A.J. Brown', 'Tyreek Hill', 'Mike Williams', 'Jarvis Landry', 'Tyler Boyd', 'A.J. Green', 'Tee Higgins']
tePool = ['Jonnu Smith']
dstPool = ['Bears', 'Packers']
flexPool = rbPool + wrPool + tePool

coreStack = ['Ryan Tannehill', 'A.J. Brown', 'Jonnu Smith']
runBack = ['Tyler Boyd','A.J. Green', 'Tee Higgins']

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

print('QB' + '\t' + 'RB' + '\t' + 'WR' + '\t' + 'TE' + '\t' + 'DST')

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
                                                        print(len(lineups))
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
for x in range(len(uniqueLineups)):
    if(set(coreStack).issubset(set(uniqueLineups[x]))):
        runBackCount = 0
        for y in range(len(runBack)):
            if(runBack[y] in uniqueLineups[x]):
                runBackCount+=1
        if (runBackCount <= runBackLimit) and (runBackCount >= 1):
            tmpLineups.append(uniqueLineups[x])
    #for w in range uniqueLineups[x]:
        
for x in range(len(tmpLineups)):
    print(x)
    print(tmpLineups[x])
    #print(uniqueLineupsID[x])
    
#for x in range(len(uniqueLineups)):
#    print(x)
#    print(uniqueLineups[x])
#    print(uniqueLineupsID[x])