#Elahi, Tanzim
#group mems: Tanzim, David
#softdev,  pd1
#Jinja tuning

from flask import Flask, render_template
import random
newCopy=open('occupations.csv','r')
text=newCopy.readlines()
dictionary=dict()
for x in text[ 1: len(text)-1]:
    i=x.strip('\n').strip('"').split(',')
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
newCopy.close()
app=Flask(__name__)
@app.route('/occupyflaskst')
def Go():
  return render_template("template.html",job=randomjob(),coll=dictionary)
if (__name__=="__main__"):
    app.debug=True
    app.run()
