#filename: BJPoject
#Purpose: To play a game of blackjack
#Programmer: Trevor Bingaman
from random import*
def createDeck():
    deck0 = [('Ace','Diamond'), ('Two','Diamond'), ('Three','Diamond'),\
             ('Four','Diamond'), ('Five','Diamond'), ('Six','Diamond'),\
             ('Seven','Diamond'), ('Eight','Diamond'), ('Nine','Diamond'),\
             ('Ten','Diamond'), ('Jack','Diamond'), ('Queen','Diamond'),\
             ('King','Diamond'), ('Ace','Club'),('Two','Club'),\
             ('Three','Club'), ('Four','Club'), ('Five','Club'), ('Six','Club'),\
             ('Seven','Club'), ('Eight','Club'), ('Nine','Club'), ('Ten','Club'),\
             ('Jack','Club'), ('Queen','Club'), ('King','Club'),\
             ('Ace','Heart'), ('Two','Heart'), ('Three','Heart'), ('Four','Heart'),\
             ('Five','Heart'), ('Six','Heart'), ('Seven','Heart'), ('Eight','Heart'),\
             ('Nine','Heart'), ('Ten','Heart'), ('Jack','Heart'), ('Queen','Heart'),\
             ('King','Heart'), ('Ace','Spade'), ('Two','Spade'), ('Three','Spade'),\
             ('Four','Spade'), ('Five','Spade'), ('Six','Spade'), ('Seven','Spade'),\
             ('Eight','Spade'), ('Nine','Spade'), ('Ten','Spade'), ('Jack','Spade'),\
             ('Queen','Spade'), ('King','Spade')]
    vdeck0 = [1,2,3,4,5,6,7,8,9,10,10,10,10,\
              1,2,3,4,5,6,7,8,9,10,10,10,10,\
              1,2,3,4,5,6,7,8,9,10,10,10,10,\
              1,2,3,4,5,6,7,8,9,10,10,10,10]
    n=len(deck0)
    ideck0=[]
    for t in range(n):
        ideck0.append(t)
    return deck0, vdeck0, ideck0

def shuffleDeck(deck0,vdeck0,ideck0):
    n = len(deck0)
    ideck1 = ideck0[:]
    vdeck1 = vdeck0[:]
    deck1 = deck0[:]
    shuffle(ideck1) 
    for t in range(n):
        deck1[t] = deck0[ideck1[t]]
        vdeck1[t] = vdeck0[ideck1[t]]
    return deck1,vdeck1,ideck1

def dealCardHouse(deck1,vdeck1,ideck1,cardh,vcardh,icardh,sumh,j,countaceh,aceh):
    cardh.append(deck1[j])
    icardh.append(ideck1[j])
    a = vdeck1[j]
    vcardh.append(a)
    if a==1:
        aceh=aceh+1
        s=sumh+11
        if aceh==1:
            if s>=17 and s<=21:
                sumc=s
                countaceh=11
            else:
                sumc=sumh+1
                countaceh=1
        else:
            sumc=sumh+1
    else:
        if aceh==0:
            sumc=sumh+a
        else:
            s=sumh+a+10
            if countaceh==1:
                s=sumh+a+10
                if s>=17 and s<=21:
                    sumc=s
                    countaceh=11
                else:
                    sumc=sumh+a

    return sumc, aceh, countaceh

def dealCardPlayer(deck1,vdeck1,ideck1,cardp,vcardp,icardp,sump,j,acep,countacep):
    cardp.append(deck1[j])
    icardp.append(ideck1[j])
    a = vdeck1[j]
    vcardp.append(a)
    if a==1:
        acep=acep+1
        s=sump+11
        if acep==1:
            if s>=17 and s<=21:
                sumc=s
                countacep=11
            else:
                sumc=sump+1
                countacep=1
        else:
            sumc=sump+1
    else:
        if acep==0:
            sumc=sump+a
        else:
            s=sump+a+10
            if countacep==1:
                s=sump+a+10
                if s>=17 and s<=21:
                    sumc=s
                    countacep=11
                else:
                    sumc=sump+a

    return sumc, acep, countacep
def main():
#1.
    deck0,vdeck0,ideck0=createDeck()
    deck0 = deck0*2
    vdeck0 = vdeck0*2
    n = len(ideck0)
    for t in range(n):
        ideck0.append(n+t)
    n = len(deck0)
    
#2.
    print("Index   Value    (Rank,Suit)")
    for t in range(n):
        print("{0:3}  {1:2}   {2}".format(ideck0[t],vdeck0[t],deck0[t]))
#3.
    deck1,vdeck1,ideck1=shuffleDeck(deck0,vdeck0,ideck0)
#4.
    print("\n\nShuffled deck:")
    print("Index  Value    (Rank,Suit)")
    for t in range(n):
        print("{0:3}  {1:2}   {2}".format(ideck1[t],vdeck1[t],deck1[t]))
#5.
    vcardh = []
    icardh = []
    cardh = []
    vcardp = []
    icardp = []
    cardp = []
    sumh = 0
    sump = 0
#6.
    j = 0
    countaceh = 0
    aceh = 0
    countaceh, aceh, sumh = dealCardHouse(deck1,vdeck1,ideck1,cardh,vcardh,icardh,sumh,j,countaceh,aceh)
    t = len(cardh)-1
    print("\n\n")
    print("Index   BJ_Value    (Rank,Suit)")
    print("House {0:2}     {1:2}    {2:3}      {3}".format(icardh[t],vcardh[t],sumh,cardh[t]))
#7.
    j = j + 1
    countacep = 0
    acep = 0
    countacep, acep, sump = dealCardPlayer(deck1,vdeck1,ideck1,cardp,vcardp,icardp,sump,j,countacep,acep)
    t = len(cardp)-1
    print("House {0:2}     {1:2}    {2:3}      {3}".format(icardp[t],vcardp[t],sump,cardp[t]))

#8.
    j = j + 1
    countaceh, aceh, sumh = dealCardHouse(deck1,vdeck1,ideck1,cardh,vcardh,icardh,sumh,j,countaceh,aceh)
    tt = len(cardh) - 1
#9.
    j = j + 1
    sump,acep,countacep=dealCardPlayer(deck1,vdeck1,ideck1,cardp,vcardp,icardp,sump,j,acep,countacep)
    t = len(cardp) - 1
    print("House {0:2}     {1:2}    {2:3}      {3}".format(icardp[t],vcardp[t],sump,cardp[t]))
#10.
    choose = input('Do you want a card? (Answer: yes or no):')
    j = j + 1
    while choose == 'yes' and j<n:
        sump,acep,countacep=dealCardPlayer(deck1,vdeck1,ideck1,cardp,vcardp,icardp,sump,j,acep,countacep)
        t = len(cardp)-1
        print("House {0:2}     {1:2}    {2:3}      {3}".format(icardp[t],vcardp[t],sump,cardp[t]))
#11.
        if sump >= 21:
            choose = 'no'
        else:
            choose = input('Do you want a card? (Answer: yes or no):')
        j = j + 1
    print("House {0:2}     {1:2}    {2:3}      {3}".format(icardh[tt],vcardh[tt],sumh,cardh[tt]))
    choose = 'yes'
    if sumh>=17:
        choose = 'no'
#12.
    while choose == 'yes' and j<n:
        countaceh, aceh, sumh = dealCardHouse(deck1,vdeck1,ideck1,cardh,vcardh,icardh,sumh,j,countaceh,aceh)
        t=len(cardh)-1
        print("House {0:2}     {1:2}    {2:3}   {3}".format(icardh[t],vcardh[t],sumh,cardh[t]))
        j=j+1
        if sumh >= 17:
            choose = 'no'
    print('')
#13.
    if sumh > 21:
        print('Player wins.')
    elif sump > 21:
        print('House wins')
    else:
        if sump > sumh:
            print('Player wins.')
        elif sumh > sump:
            print('House wins.')
        else:
            print('Tie.')
main()

