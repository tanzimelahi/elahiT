#elizabeth participated with both me and amber which is why her name
#appears on both of ours repo.However, amber and I came up with different
#algorithms and as far as I know elizabeth submitted the work she had created
#with amber in her repo.This is the algorithm that she and I created
import random
newCopy=open('occupations.csv','r')
text=newCopy.readlines()
dictionary=dict()
for x in text[ 1: len(text)-1]:
    i=x.strip('\n').split(',')
    dictionary[i[0]]=float(i[len(i)-1])

def randomjob():
    collection=list()
    collection.append(list(dictionary.values())[0])
    for key in list(dictionary.values())[1:]:
        collection.append(round(key+collection[len(collection)-1],1))

    #the random part
    number=random.random()*collection[len(collection)-1]
    #print (collection)
    #print (number)
    timer=-1
    #print (list(dictionary.values()))
    for x in collection:
        if x-number>0:
            if timer!=-1:
                x=round(x-collection[timer],1)
                #print (x)
            for y in list(dictionary.keys()):
                if dictionary[y]==x:
                     return y

        timer=timer+1
print (randomjob())
newCopy.close()
