#Dan Merrifield

import csv
import itertools
from collections import Counter

salaryLimit = 50000
salaryWaste = 500

headers = ['CPT', 'FLEX', 'FLEX', 'FLEX', 'FLEX', 'FLEX']

cptPool = ['Scotty Miller', 'Darius Slayton', 'Buccaneers', 'Rob Gronkowski']
flexPool = ['Darius Slayton', 'Sterling Shepard', 'Leonard Fournette', 'Tom Brady', 'Scotty Miller', 'Buccaneers', 'Wayne Gallman Jr.', 'Daniel Jones', 'Mike Evans', 'Rob Gronkowski', 'Cameron Brate', 'Golden Tate']

output = '/Users/dmerrifield/lineups.csv'

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

print('CPT' + '\t' + 'FLEX' + '\t' + 'FLEX' + '\t' + 'FLEX' + '\t' + 'FLEX'+ '\t' + 'FLEX')
    
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
        
for x in lineupsID:
    srtd = tuple(sorted(x))
    if srtd not in seen:
        uniqueLineupsID.append(x)
        seen.add(srtd)

#for x in range(len(uniqueLineupsID)):
    #print(x)
    #print(uniqueLineups[x])
    #print(uniqueLineupsID[x])
    #for y in uniqueLineupsID[x]:
        #print(player[y].id)        
        
with open(output, 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(headers)
    for x in range(len(uniqueLineupsID)):
        tmpLineup=[]
        for y in uniqueLineupsID[x]:
            tmpLineup.append(player[y].id)
        print(tmpLineup) 
        wr.writerow(tmpLineup)
