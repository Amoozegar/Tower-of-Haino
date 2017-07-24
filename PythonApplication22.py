import random
import numpy as np
import math

M=6
Stacks=[]
N=6
T=256


for i in range(M):
    Stacks.append([])
for i in range(N):
    Stacks[0].append(N-i)
emptyStacks=[]

for i in range(M):  #determine empty stacks
    if i!=0:
        emptyStacks.append(i)

NonEmptyStacks=[]
NonEmptyStacks.append(0)

lastDisk=[]
for i in range(N):
    lastDisk.append(0)
lastDisk[0]=N

Moves={}
for i in range(M):              # determining the dictionary of possible moves
    if i!=0 and i!=M-1:
        Moves[i]=[i-1, i+1]
    if i==0:
        Moves[i]=[1]
    if i==M-1:
        Moves[i]=[M-2]

def CreatMove(start,i):
    Moveslist=[]
    Moveslist.append(start)
    Moveslist.append(i)
    PossibleMoves.append(Moveslist)
CenterOfMass=[] 
for t in range(T):
    PossibleMoves=[]  #possible moves that can be make at each iteration
    for i in range(M):  #finding the most recent disk
        if i in NonEmptyStacks:
            lastDisk[i]=Stacks[i][len(Stacks[i])-1]

    for i in NonEmptyStacks:
        
        start=i    #the starting stack
        for j in Moves[start]:
                
            if j in emptyStacks:
                CreatMove(start,j) 
                
            elif j in NonEmptyStacks:
                if lastDisk[start]<lastDisk[j]:
                    CreatMove(start,j)
    SelectedMove=random.choice(PossibleMoves) 
   
    StartStack=SelectedMove[0]  
    if len(Stacks[StartStack])==1:         # the stack at origin
        emptyStacks.append(StartStack)
        NonEmptyStacks.remove(StartStack)  
    DestStack=SelectedMove[1] 
    if len(Stacks[DestStack])==0:         # the stack at destination
        emptyStacks.remove(DestStack)
        NonEmptyStacks.append(DestStack)             
    Stacks[DestStack].append(Stacks[StartStack][len(Stacks[StartStack])-1])
    Stacks[StartStack].remove(Stacks[StartStack][len(Stacks[StartStack])-1]) 
    Elm=[]
    SigmaNom=[]
    for i in NonEmptyStacks:
        p=i
        SigmaNom.append(sum(np.multiply(Stacks[i],p)))
    SigmaDenom=0 
    for k in range(N):
        SigmaDenom = SigmaDenom +k+1

    CenterOfMass.append(float(sum(SigmaNom))/float(SigmaDenom))
Mean=float(sum(CenterOfMass))/float(T)
NomVar=[]
for l in CenterOfMass:
    NomVar.append((Mean-l)**2)
Var=float(sum((NomVar)))/float(T)
StDev = math.sqrt(Var)
print ('%.10f' %Mean)
print ('%.10f' %StDev)