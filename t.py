#coding:utf-8
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
    if not len(maincolor):
        for i in range(len(card)):
            if card[i][0]!="e" and card[i][0]!="w":
                maincolor = card[i][0]
    maxindex = -1
            
    for i in range(len(card)):
        w = card[i][0].find("w")
        if w!=-1:
            maxindex = i
            break
    
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
                minorcolor = card[i][0]
                maxindex = i
            if minorcolor != "e" and card[i][0] == minorcolor:
                if int(card[i][1:])>int(card[maxindex][1:]):
                    maxindex = i
    
    if maxindex == -1:
        maxindex = 0
                
    return maxindex
                
class player(object):
    def __init__(self,name,card=[],noround=[],noplayer=[],maincolor=[]):
        self.name = name
        self.card = card
        self.noround = 1
        self.nocard = len(card)
        self.maincolor = maincolor
        self.notrick = 0
        self.noplayer = noplayer
        
    def sortcard(self):
        colororder1 = ["w",self.maincolor,"h","d","s","c","e"]
        colororder = []
        for a in colororder1:
            if a not in colororder:
                colororder.append(a)
        
        self.card.sort(key=lambda x:int(x[1:]),reverse=True)
        
        newcard = []
        for color in colororder:
            for card in self.card:
                if card[0] == color:
                    newcard.append(card)
        self.card = newcard
        
    def playcard(self,card):
        try:
            self.card.remove(card)
            self. nocard = self.nocard -1
        except:
            print "this card not in your hand"

        
            
class NPC(player):
    def playcard(self):
        card = random.sample(self.card,1)
        self.card.remove(card)
        self.nocard=self.nocard-1
        return card
        
    
        
            
            
    
def maingame():
    print "欢迎来到神机妙算游戏！"
    print "-by 天望"
    while 1:
        noplayer = raw_input("请输入游戏人数（2-6）：")
        try:
            noplayer = int(noplayer)
        except:
            print "请输入数字"
        if noplayer<1 or noplayer>7:
            print "请输入2-6之间的数字"
            continue
        break 
            
    npc=[]
    for i in range(noplayer):
        npc.append(NPC("npc"+str(i)))
    
    noround=60/noplayer
    banker = random.randint(0,noplayer-1)
    for i in range(noround ):
        alreadycard = []
        maincolor = []
        
        banker = banker+1
        if banker>noplayer-1:
            banker =0
            
            
        for a in npc:
            a.card = dealcard(i+1,alreadycard)
            alreadycard = alreadycard + a.card
        if len(alreadycard)!=60:
            maincolor = dealcard(1,alreadycard)
            maincolor = maincolor[0]
        if maincolor == "e":
            maincolor =[]
            
        
        
        print "当前为第%d轮，首先出牌者为%s" % (i+1,npc[banker].name)
        print "您的手牌为："
        npc[0].sortcard()
        print npc[0].card
        while 1:
            a= raw_input("请输入您本轮所叫墩数：")
            try:
                npc[0].notrick=int(a)
                break
            except:
                print " 请输入数字"
        
        
    
        
        
        
            
        
        
        
        
        
        
        
if __name__ == '__main__':
    maingame()