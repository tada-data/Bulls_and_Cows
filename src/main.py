from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("main.html")

@app.route("/start", methods=["GET","POST"])
def start():
    number = [0,1,2,3,4,5,6,7,8,9]
    answer_list = random.sample(number,4)
    answer = str(answer_list[0])+str(answer_list[1])+str(answer_list[2])+str(answer_list[3])
    return render_template("game.html", answer=answer)


@app.route("/reset", methods=["POST","GET"])
def again():
    if request.method == "GET":
        return render_template("game.html")

    else:
        user = request.form["usernumber"]
        answer = request.form["answer"]
        global user_list
        user_list=[]

        strike = {}
        for i in range(4):
            if answer[i]==user[i]:
                strike[answer[i]]="strike"

        ball = {}
        for num in answer:
            for i in range(4):
                if user[i]==num:
                    ball[num]="ball"
                    
        for key in list(strike.keys()):
            del(ball[key])
            
        strike_num = len(strike)
        ball_num = len(ball)

        if (strike_num==0)&(ball_num==0):
            show = "out"
        else:
            show = str(strike_num)+"S"+" "+str(ball_num)+"B"
        user_list.append(user+" : "+show)


        if show == "4S 0B":
            return render_template("correct.html", user_list=user_list)
        
        else:
            return render_template("again.html", show=show, user=user, answer=answer, user_list=user_list)


@app.route("/game", methods=["POST","GET"])
def game():
    if request.method == "GET":
        return render_template("game.html")

    else:
        user = request.form["usernumber"]
        answer = request.form["answer"]

        strike = {}
        for i in range(4):
            if answer[i]==user[i]:
                strike[answer[i]]="strike"

        ball = {}
        for num in answer:
            for i in range(4):
                if user[i]==num:
                    ball[num]="ball"
                    
        for key in list(strike.keys()):
            del(ball[key])
            
        strike_num = len(strike)
        ball_num = len(ball)

        if (strike_num==0)&(ball_num==0):
            show = "out"
        else:
            show = str(strike_num)+"S"+" "+str(ball_num)+"B"
        user_list.append(user+" : "+show)

        chance=len(user_list)

        if show == "4S 0B":
            return render_template("correct.html", chance=chance)
        
        else:
            return render_template("again.html", show=show, user=user, answer=answer, user_list=user_list)


if __name__=="__main__":
    app.run()