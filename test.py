import random

def dealcard(num,alreadycard=[]):
    allcard = ["w1","w2","w3","w4","e1","e2","e3","e4"]
    for color in ["h","d","s","c"]:
        for i in range(13):
            allcard.append(color+str(i+1))
    remaincard = list(set(allcard) - set(alreadycard))
    selectcard = random.sample(remaincard,num)
    
    return selectcard
    
if __name__ == '__main__':
    a=["w1","c4"]
    print dealcard(58)
    