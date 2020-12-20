from flask import Flask, render_template, request, redirect
from random import randint
app = Flask(__name__)

@app.route("/")
def input_data2():
    return render_template('home.html')

@app.route("/teacher")
def input_data67():
    return render_template('teacher.html')

@app.route("/<mode>")
def input_data(mode):
        with open('keylist.data','r')as fil:data=fil.read()
        data=data.split('\n')
        for i in range(len(data)):
            data[i] = data[i].split(',')
        while True:
            try:data.remove([''])
            except:break
        for i in range(len(data)):
            if mode == data[i][0]+data[i][1]:
                try:
                    with open(data[i][0]+'_records.data','r') as fil:data=fil.read()
                    data=data.replace('\n','<br>')
                    data=data.replace('|','     ')
                    return data
                except:return render_template('error.html', message='No Data Entry')
            if mode==data[i][0]:
                with open(mode+'.data','r')as fil:x=fil.read()
                x=x.split('\n')
                x.remove('')
                for i in range(len(x)):
                    x[i]=x[i].split('|')
                return render_template('q10.html', Id = mode,Q1=x[0][0],Q2=x[1][0],Q3=x[2][0],Q4=x[3][0],Q5=x[4][0],Q6=x[5][0],Q7=x[6][0],Q8=x[7][0],Q9=x[8][0],Q10=x[9][0])


@app.route("/",methods = ['GET','POST'])
def getvalue():
    try:
        try:
            mode=request.form['code']
            with open(mode+'.data','r')as fil:x = fil.read()
            return redirect("https://onlinetestbyprakhar.pythonanywhere.com/"+mode)
        except:
            lst=[[request.form['q1'],request.form['ans1']],[request.form['q2'],request.form['ans2']],
                 [request.form['q3'],request.form['ans3']],[request.form['q4'],request.form['ans4']],
                 [request.form['q5'],request.form['ans5']],[request.form['q6'],request.form['ans6']],
                 [request.form['q7'],request.form['ans7']],[request.form['q8'],request.form['ans8']],
                 [request.form['q9'],request.form['ans9']],[request.form['q10'],request.form['ans10']]]
            choices = ['Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','C','B','A','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','9','8','7','6','5','4','3','2','1','0']
            with open('keylist.data','r')as fil:keys = fil.read()
            key=''
            while key in keys:
                key,key2='',''
                for i in range(5):key += choices[randint(0,len(choices)-1)]
                for i in range(3):key2 += choices[randint(0,len(choices)-1)]
                with open('keylist.data','a+')as fil:fil.write(key+','+key2+'\n')
                with open(str(key)+'.data','w+')as fil:
                    for i in range(len(lst)):
                        fil.write(lst[i][0]+'|'+lst[i][1]+'\n')
            return render_template('error2.html', message='https://onlinetestbyprakhar.pythonanywhere.com/'+key, message2 = 'https://onlinetestbyprakhar.pythonanywhere.com/'+key+key2, message3 = key)
        finally:return render_template('error.html', message='Form Does not Exist')
    except:
        ids = request.form['myid']
        details = request.form['Sname']+'|'+request.form['Sroll']+'|'+request.form['Sclass']+'|'
        lst = [request.form['a1'],request.form['a2'],request.form['a3'],request.form['a4'],
               request.form['a5'],request.form['a6'],request.form['a7'],request.form['a8'],
               request.form['a9'],request.form['a10']]
        with open(ids+'.data','r')as fil:data=fil.read()
        data=data.split('\n')
        data.remove('')
        for i in range(len(data)):data[i]=data[i].split('|')
        c=0
        for i in range(10):
            if data[i][1] == lst[i]:c+=1
        with open(ids+'_records.data','a+') as fil:
            fil.write(details+str(c)+"/10"+'\n')
        return render_template('error.html', message='You Scored - '+str(c)+"/10")

if __name__=="__main__":
    app.run()
