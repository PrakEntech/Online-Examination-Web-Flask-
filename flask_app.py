from flask import Flask, render_template, request
from random import randint
app = Flask(__name__)

@app.route("/")
def input_data2():
    return render_template('home.html')

@app.route("/teacher")
def input_data67():
    return render_template('mcqInput.html')

@app.route("/submission")
def input_data890():
    return render_template('submission.html')

@app.route("/teacher/fill",methods = ['GET','POST'])
def getvalue():
    quests,correct,options,temp=[],[],[],[]
    for i in range(1,11):
        temp=[]
        quests.append(request.form[str(i)+'q'])
        correct.append(request.form['co'+str(i)])
        for j in range(1,5):
            temp.append(request.form[str(i)+'q'+str(j)])
        options.append(temp)
    choices = ['Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','C','B','A','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','9','8','7','6','5','4','3','2','1','0']
    with open('keylist.data','r')as fil:keys = fil.read()
    key=''
    while key in keys:
        key,key2='',''
        for i in range(5):key += choices[randint(0,len(choices)-1)]
        for i in range(3):key2 += choices[randint(0,len(choices)-1)]
    with open('keylist.data','a+')as fil:fil.write(key+','+key2+'\n')
    with open(str(key)+'.data','w+')as fil:
        for i in range(len(quests)):
            fil.write(quests[i]+'|')
            for j in range(len(options[i])):
                fil.write(options[i][j]+'|')
            fil.write(correct[i]+'\n')
    return render_template('error2.html', message=key, message2=key+key2)

@app.route("/formsubmit",methods = ['GET','POST'])
def getvalue3():
                key=request.form['code']
                try:
                    with open(key+'.data','r')as fil:data=fil.read()
                    data=data.split('\n')
                    data=data[:len(data)-1]
                    for i in range(len(data)):data[i]=data[i].split('|')
                    return render_template('asdqwe.html',
                           Q1=data[0][0],
                           q1q1=data[0][1],
                           q1q2=data[0][2],
                           q1q3=data[0][3],
                           q1q4=data[0][4],
                           Q2=data[1][0],
                           q2q1=data[1][1],
                           q2q2=data[1][2],
                           q2q3=data[1][3],
                           q2q4=data[1][4],
                           Q3=data[2][0],
                           q3q1=data[2][1],
                           q3q2=data[2][2],
                           q3q3=data[2][3],
                           q3q4=data[2][4],
                           Q4=data[3][0],
                           q4q1=data[3][1],
                           q4q2=data[3][2],
                           q4q3=data[3][3],
                           q4q4=data[3][4],
                           Q5=data[4][0],
                           q5q1=data[4][1],
                           q5q2=data[4][2],
                           q5q3=data[4][3],
                           q5q4=data[4][4],
                           Q6=data[5][0],
                           q6q1=data[5][1],
                           q6q2=data[5][2],
                           q6q3=data[5][3],
                           q6q4=data[5][4],
                           Q7=data[6][0],
                           q7q1=data[6][1],
                           q7q2=data[6][2],
                           q7q3=data[6][3],
                           q7q4=data[6][4],
                           Q8=data[7][0],
                           q8q1=data[7][1],
                           q8q2=data[7][2],
                           q8q3=data[7][3],
                           q8q4=data[7][4],
                           Q9=data[8][0],
                           q9q1=data[8][1],
                           q9q2=data[8][2],
                           q9q3=data[8][3],
                           q9q4=data[8][4],
                           Q10=data[9][0],
                           q10q1=data[9][1],
                           q10q2=data[9][2],
                           q10q3=data[9][3],
                           q10q4=data[9][4],
                           Id=key
                           )
                except:return render_template('error.html', message='Wrong Form Code')

@app.route("/formresult",methods = ['GET','POST'])
def getvalue2():
    options=[]
    key=request.form['key']
    name=request.form['Sname']
    class1=request.form['Sclass']
    roll=request.form['Sroll']
    for i in range(1,11):
        options.append(request.form[str(i)+'q'])
    with open(key+'.data','r')as fil:
        data=fil.read()
    data=data.split('\n')
    data=data[:len(data)-1]
    for i in range(len(data)):data[i]=data[i].split('|')
    score=0
    for i in range(len(data)):
        if data[i][5]==options[i]:score+=1
    print(score)
    with open(key+'_records.data','a+') as fil:fil.write(name+' '+class1+' '+roll+' '+str(score)+'/10\n')
    return render_template('error.html',message='You Scored - '+str(score)+'/10')

@app.route("/checksubmissions",methods = ['GET','POST'])
def getvalue90():
                mode=request.form['cool']
                mode2 = mode[:5]
                with open('keylist.data','r')as fil:data=fil.read()
                data=data.split('\n')
                for i in range(len(data)):
                    data[i] = data[i].split(',')
                while True:
                    try:data.remove([''])
                    except:break
                z='1'
                for i in range(len(data)):
                    if mode == data[i][0]+data[i][1]:
                        z='2'
                        with open(mode2+'_records.data','r') as fil:data=fil.read()
                        data=data.replace('\n','<br>')
                        data=data.replace('|','     ')
                        return data
                if z=='1':
                    return render_template('error.html', message='Wrong Submission Code')

if __name__=="__main__":
    app.run()
