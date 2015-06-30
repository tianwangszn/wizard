import random

def dealcard(num,alreadycard=[]):
    allcard = ["w1","w2","w3","w4","e1","e2","e3","e4"]
    for color in ["h","d","s","c"]:
        for i in range(13):
            allcard.append(color+str(i+1))
    remaincard = list(set(allcard) - set(alreadycard))
    selectcard = random.sample(remaincard,num)
    
    return selectcard
    
    
def comparecard(card,maincolor=[]):
    if len(maincolor):
        for i in range(len(card)):
            if card[i][0]!="e" and card[i][0]!="w":
                maincolor = card[i][0]
    maxindex = -1
            
    for i in range(len(card)):
        w = card[i][0].find("w")
        if w!=-1:
            maxindex = i
    
    if maxindex == -1:
        for i in range(len(card)):
            if card[i][0] == maincolor:
                if maxindex == -1:
                    maxindex = i
                if int(card[i][1:])>int(card[maxindex][1:]):
                    maxindex = i
                    
    if maxindex == -1:
        minorcolor = "e"
        for i in range(len(card)):
            if card[i][0]!="e" and minorcolor =="e":
                print "aaa"
                minorcolor = card[i][0]
                maxindex = i
            if minorcolor != "e" and card[i][0] == minorcolor:
                if int(card[i][1:])>int(card[maxindex][1:]):
                    maxindex = i
    
    if maxindex == -1:
        maxindex = 0
                
    return maxindex
                
             
            
            
    
    
    
if __name__ == '__main__':
    a=["e1","e2","e3","c4"]
    print comparecard(a,['h'])
    