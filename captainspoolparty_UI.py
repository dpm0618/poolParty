#Dan Merrifield

import csv
import itertools
import random
from collections import Counter
import tkinter as tk

inputPath = 'C:\\Users\\Dan\\Downloads\\DKSalaries_captains.csv'
outputPath = 'C:\\Users\\Dan\\dvl\\poolParty\\lineups_captain.csv'

root = tk.Tk()
root.geometry('625x700')
root.configure(bg='#202245')
root.resizable(False, False)
root.title('CPT Lineup Generator')

def addPlayerToCpt():
    for x in playerList.curselection():
        if playerList.get(x) not in cptList.get(0,"end"):
            cptList.insert(cptList.size(),playerList.get(x))
            playerList.selection_clear(x)

def addPlayerToFlex():
    for x in playerList.curselection():
        if playerList.get(x) not in flexList.get(0,"end"):
            flexList.insert(flexList.size(),playerList.get(x))
            playerList.selection_clear(x)
            
def removePlayer():
    for x in cptList.curselection()[::-1]:
        cptList.delete(x)
    for x in flexList.curselection()[::-1]:
        flexList.delete(x)
        
def addAvoidPair():
    if len(cptList.curselection()) == 2:
        selection = cptList.curselection()
        pair = cptList.get(selection[0]) + ':' + cptList.get(selection[1])
        avoidPairList.insert(avoidPairList.size(), pair)
        for x in cptList.curselection():
            cptList.selection_clear(x)
    elif len(flexList.curselection()) == 2:
        selection = flexList.curselection()
        pair = flexList.get(selection[0]) + ':' + flexList.get(selection[1])
        avoidPairList.insert(avoidPairList.size(), pair)
        for x in flexList.curselection():
            flexList.selection_clear(x)
            
def addExposure():
    
    if len(cptList.curselection()) > 0:
        for x in cptList.curselection():
            #print('added exposure for ' + cptList.get(x))
            exposureList.insert(exposureList.size(), cptList.get(x))
            cptList.selection_clear(x)
            
    if len(flexList.curselection()) > 0:
        for x in flexList.curselection():
            #print('added exposure for ' + flexList.get(x))
            exposureList.insert(exposureList.size(), flexList.get(x))
            flexList.selection_clear(x)
        
    #exposureCount = exposureList.size()
    printExposureSliders()
        
def printExposureSliders():
    for x in range(0,len(exposureSlider)):
        #if x >= exposureList.size():
        exposureSlider[x].destroy()
        del exposureSlider[x]
        exposureLabel[x].destroy()
        del exposureLabel[x]
            
    #exposureCount = len(exposureLabel)
    exposureCount = 0
    print(str(exposureCount))
    #for x in exposureList.get(len(exposureLabel), exposureList.size()):
    for x in exposureList.get(0, exposureList.size()):
        exposureLabel[exposureCount] = tk.Label(root, bg='#202245', fg='white', text=exposureList.get(exposureCount).split('~')[1].lstrip())
        print(exposureList.get(exposureCount))
        exposureLabel[exposureCount].place(x=375,y=(525 + (35 * exposureCount)))
        
        exposureSlider[exposureCount] = tk.Scale(root, bg="#b4b5d4", from_=0, to=100, resolution=5, width=10, length=100, orient="horizontal")
        exposureSlider[exposureCount].place(x=500,y=(525 + (35 * exposureCount)))
        exposureSlider[exposureCount].set(100)
        
        exposureCount+=1
    
            
def removeAvoidPair():
    if avoidPairList.size() > 0:
        for x in avoidPairList.curselection()[::-1]:
            avoidPairList.delete(x)

def removeExposure():
    if exposureList.size() > 0:
        for x in exposureList.curselection()[::-1]:
            exposureList.delete(x)
        printExposureSliders()

def runGenerator():
    setQBCount = True
    
    outputText.delete(1.0, "end")
    outputText.insert("end", "\nGENERATING LINEUPS\n")
    outputText.see("end")
    
    salaryMax = int(salaryMaxText.get(1.0,"end"))
    salaryMin = int(salaryMinText.get(1.0,"end"))
    
    cptPool = []
    cptPoolID = []
    for x in cptList.get(0,cptList.size()):
        cptPool.append(x.split('~')[1].lstrip())
        print (x.split('~')[1].lstrip())
        
    flexPool = []
    flexPoolID = []
    for x in flexList.get(0,flexList.size()):
        flexPool.append(x.split('~')[1].lstrip())
        print (x.split('~')[1].lstrip())
        
    for x in range(len(cptPool)):
        for y in range(len(player)):
            if (player[y].name.strip() == cptPool[x].strip()) and (player[y].type == 'CPT'):
                cptPoolID.append(y)
                print('added ' + player[y].name + ' as CPT')
                
    for x in range(len(flexPool)):
        for y in range(len(player)):
            if (player[y].name.strip() == flexPool[x].strip()) and (player[y].type == 'FLEX'):
                flexPoolID.append(y)
                print('added ' + player[y].name + ' as FLEX')
        
    print(cptPoolID)
    print(flexPoolID)
    
    lineupCount = 0
    lineups = []
    lineupsID = []
    
    for cpt in range(len(cptPool)):
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
                                                if (salaryTotal <= salaryMax) and (salaryTotal > salaryMin):
                                                    #print(len(lineups))
                                                    #print(lineupCount)
                                                    #print(tmpLineup)
                                                    #print(salaryTotal)
                                                    lineups.append(tmpLineup)
                                                    #flexLineup.append(tmpFlexLineup)
                                                    lineupsID.append(tmpLineupID)
                                                    #flexLineupID.append(tmpFlexLineupID)
                                                    #salary.append(salaryTotal)
                                                    lineupCount+=1
                                                            
    seen = set()
    uniqueLineups = []
    uniqueLineupsID = []
     
    count=0
    for x in lineupsID:
        srtd = tuple(sorted(x))
        if srtd not in seen:
            uniqueLineupsID.append(x)
            uniqueLineups.append(lineups[count])
            seen.add(srtd)
        count+=1
    
    #shuffle    
    if setShuffle:

        merged = list(zip(uniqueLineups,uniqueLineupsID))
        random.shuffle(merged)
        uniqueLineups, uniqueLineupsID = zip(*merged)
        
    if avoidPairList.size() > 0:
    
        print("\nChecking for avoided pairs")
        
        tmpLineups = []
        tmpLineupsID = []
        
        for x in avoidPairList.get(0, "end"):
            avoidA = x.split(':')[0].split('~')[1].lstrip()
            avoidB = x.split(':')[1].split('~')[1].lstrip()
            print('avoiding lineups with ' + avoidA + ' and ' + avoidB)
            for y in range(len(uniqueLineupsID)):    
                if avoidA not in uniqueLineups[y] or avoidB not in uniqueLineups[y]:
                    tmpLineups.append(uniqueLineups[y])
                    tmpLineupsID.append(uniqueLineupsID[y])
        
            uniqueLineups = tmpLineups
            uniqueLineupsID = tmpLineupsID
            tmpLineups = []
            tmpLineupsID = []
            
    if exposureList.size() > 0:
    
        print("\nChecking exposure")
        print(len(uniqueLineups))
        print(len(uniqueLineupsID))
        
        tmpLineups = []
        tmpLineupsID = []
        
        # for now just determine if the lineups do not contain any player in our exposure pool.
        # this allows us to accurately determine how many lineups of each participant will be allowed after pruning. 
        
        for x in range(len(uniqueLineupsID)):

            validLineup = True
            exposureCount = 0

            for y in exposureList.get(0, exposureList.size()):

                playerName = exposureLabel[exposureCount].cget("text")
                playerExposure = exposureSlider[exposureCount].get()
                #print(playerName + ' with exposure ' + str(playerExposure * 100) + '%\n')
                
                if playerName in uniqueLineups[x]:
                    validLineup = False
                    
                exposureCount+=1
            
            if validLineup:
                print("Valid lineup found " + str(uniqueLineups[x]))
                tmpLineups.append(uniqueLineups[x])
                tmpLineupsID.append(uniqueLineupsID[x])
        
        #shuffledLineups = uniqueLineups
        
        baseLength = len(tmpLineups)
        
        print(str(baseLength) + " lineups without exposure-checked players")
        
        for x in range(exposureList.size()):
            exposureCount = 0
            currentCount = 0
            
            playerName = exposureLabel[x].cget("text")
            playerExposure = float(exposureSlider[x].get()) * .01
            
            #see if previous loops have already added an exposure checked player
            
            for y in range(len(tmpLineups)):
                currentCount+= tmpLineups[y].count(playerName)
            
            
            #why is this only running once for two players
            #print("player " + playerName + " with exposure of " + str(playerExposure) + " currently in " + str(currentCount) + " lineups")
                
            for y in range(len(uniqueLineupsID)):
                
                if playerName in uniqueLineups[y] and (exposureCount + currentCount) <= (baseLength * playerExposure) and uniqueLineups[y] not in tmpLineups:
                    print('exposureCount for ' + playerName + ' equal to ' + str(exposureCount + currentCount) + ' out of ' + str(baseLength * playerExposure))
                    tmpLineups.append(uniqueLineups[y])
                    tmpLineupsID.append(uniqueLineupsID[y])
                    print('adding lineup ' + str(uniqueLineups[y]))
                    exposureCount+=1
                    baseLength+=1
                    
                
        uniqueLineups = tmpLineups
        uniqueLineupsID = tmpLineupsID
        
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

    #outputText.delete(1.0, "end")
    outputText.insert("end", "\nCPT DISTRIBUTION:\n")
    for x in range(len(cptPool)):
        count = 0
        for y in range(len(uniqueLineups)):
            if cptPool[x] == uniqueLineups[y][0]:
                count+=1
        outputText.insert("end", 'CPT  ' + cptPool[x] + ':  ' + str(count) + '\n')  

    outputText.insert("end", "\nFLEX DISTRIBUTION:\n")
    for x in range(len(flexPool)):
        count = 0
        for y in range(len(uniqueLineups)):
            if flexPool[x] in uniqueLineups[y] and uniqueLineups[y].index(flexPool[x]) != 0:
                count+=1
        outputText.insert("end", 'FLEX ' + flexPool[x] + ':  ' + str(count) + '\n')  


    outputText.insert("end", '\ngenerated ' + str(len(uniqueLineupsID)) + ' unique lineups worth > $' + str(salaryMin))
    outputText.see("end")
    
    print()
    with open(outputPath, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(headers)
        for x in range(len(uniqueLineupsID)):
            tmpLineup=[]
            for y in uniqueLineupsID[x]:
                tmpLineup.append(player[y].id)
            print(tmpLineup) 
            wr.writerow(tmpLineup)
        

playerLabel = tk.Label(root, text="All Players", relief="raised", bg="#6c6d91")
playerLabel.place(x=35, y=26)

playerList = tk.Listbox(root, width=17, height=22, selectmode="multiple", bg="#b4b5d4")
playerList.place(x=25,y=50)

cptLabel = tk.Label(root, text="CPT Players", relief="raised", bg="#6c6d91")
cptLabel.place(x=210, y=26)

cptList = tk.Listbox(root, width=17, height=8, selectmode="multiple", bg="#b4b5d4")
cptList.place(x=200,y=50)

flexLabel = tk.Label(root, text="FLEX Players", relief="raised", bg="#6c6d91")
flexLabel.place(x=210, y=200)

flexList = tk.Listbox(root, width=17, height=12, selectmode="multiple", bg="#b4b5d4")
flexList.place(x=200,y=225)

avoidLabel = tk.Label(root, text="Avoid Pairs", relief="raised", bg="#6c6d91")
avoidLabel.place(x=385, y=26)

avoidPairList = tk.Listbox(root, width=25, height=8, selectmode="multiple", bg="#b4b5d4")
avoidPairList.place(x=375,y=50)

exposureLabel = tk.Label(root, text="Exposure List", relief="raised", bg="#6c6d91")
exposureLabel.place(x=385, y=200)

exposureList = tk.Listbox(root, width=25, height=8, selectmode="multiple", bg="#b4b5d4")
exposureList.place(x=375,y=225)

addCptPlayerButton = tk.Button(root, text="Add to CPT pool", command=addPlayerToCpt)
addCptPlayerButton.place(x=25, y=440)

addFlexPlayerButton = tk.Button(root, text="Add to FLEX pool", command=addPlayerToFlex)
addFlexPlayerButton.place(x=25, y=470)

runGeneratorButton = tk.Button(root, text="Run generator", command=runGenerator)
runGeneratorButton.place(x=25, y=500)

removePlayerButton = tk.Button(root, text="Remove from pool", command=removePlayer)
removePlayerButton.place(x=200, y=440)

addAvoidPairButton = tk.Button(root, text="Add avoid pair", command=addAvoidPair)
addAvoidPairButton.place(x=200, y=470)

addExposureButton = tk.Button(root, text="Add exposure check", command=addExposure)
addExposureButton.place(x=200, y=500)

removeAvoidPairButton = tk.Button(root, text="Remove avoid pair", command=removeAvoidPair)
removeAvoidPairButton.place(x=375, y=440)

removeExposureButton = tk.Button(root, text="Remove exposure", command=removeExposure)
removeExposureButton.place(x=375, y=470)

salaryMinLabel = tk.Label(root, text="Salary MIN:", bg='#202245', fg='white')
salaryMinLabel.place(x=375, y=380)

salaryMinText = tk.Text(root, height=1, width=5)
salaryMinText.place(x=475, y=380)
salaryMinText.insert("end",'49500')

salaryMaxLabel = tk.Label(root, text="Salary MAX:", bg='#202245', fg='white')
salaryMaxLabel.place(x=375, y=410)

salaryMaxText = tk.Text(root, height=1, width=5)
salaryMaxText.place(x=475, y=410)
salaryMaxText.insert("end",'50000')

#sliderTest = tk.Scale(root, from_=0, to=100, resolution=5, width=10, length=100, orient="horizontal")
#sliderTest.place(x=500, y=500)

exposureSlider = {}
exposureLabel = {}

outputText = tk.Text(root, height=10, width=45, bg="#b4b5d4")
outputText.place(x=25, y=535)

#salaryLimit = 50000
#salaryWaste = 500

exposureCount = 0

setExposure = False
setAvoidPairs = False
setQBCount = False
#Shuffling will only impact the output if setExposure = True
setShuffle = True

lineupCount=0
lineups=[]
lineupsID=[]

qbMin = 1
qbMax = 2

headers = ['CPT', 'FLEX', 'FLEX', 'FLEX', 'FLEX', 'FLEX']

#cptPool = ['Cooper Kupp','Matthew Stafford','Joe Burrow','Ja\'Marr Chase','Joe Mixon']
#flexPool = ['Cooper Kupp','Matthew Stafford','Joe Burrow','Ja\'Marr Chase','Joe Mixon','Odell Beckham Jr.','Tee Higgins','Cam Akers','Tyler Boyd','Van Jefferson','Kendall Blanton','Drew Sample','Evan McPherson','Matt Gay','Rams','Samaje Perine','Bengals','Sony Michel']

#exposure = ['DeVonta Smith:30']
#exposure = ['Drew Sample:30','Rams:25','Bengals:25','Samaje Perine:25','Kendall Blanton:40','Sony Michel:25']

#avoidPairs = ['Mike Evans:Chris Godwin']
#avoidPairs = ['Evan McPherson:Matt Gay','Van Jefferson:Odell Beckham Jr.','Ja\'Marr Chase:Joe Mixon','Tee Higgins:Tyler Boyd','Kendall Blanton:Drew Sample','Matt Gay:Matthew Stafford','Evan McPherson:Joe Burrow','Rams:Joe Burrow','Samaje Perine:Joe Mixon','Bengals:Matthew Stafford','Sony Michel:Cam Akers']

#output = '/Users/Dan/lineups_captain.csv'

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
                    player.append(Player(row[2], row[5], row[0], row[7], row[1], row[4], count))
                    value = row[0] + " ~ " + row[2]
                    if value not in playerList.get(0,"end"):
                        playerList.insert(playerList.size(),row[0] + " ~ "+ row[2])
                    #print(player[count].name)
                count+=1
                
            print()    
            self.details = list(csv_input)

    def get_col_row(self, col, row):
        return self.details[row-1][col-1]
    
class Player:
    def __init__(self, name, salary, position, team, id, type, rowNum):
        self.name = name
        self.salary = salary
        self.position = position
        self.team = team
        self.id = id
        self.type = type
        self.rowNum = rowNum
        
    #def get_salary_by_name(self, name):
        #if self.name == name

player = []

data = PlayerDetails(inputPath)

lineupCount = 10
cptPoolID = []
flexPoolID = []

root.mainloop()


#print('CPT' + '\t' + 'FLEX' + '\t' + 'FLEX' + '\t' + 'FLEX' + '\t' + 'FLEX'+ '\t' + 'FLEX')

       
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
