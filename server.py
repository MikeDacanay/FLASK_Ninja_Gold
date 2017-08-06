from flask import Flask, request, render_template, redirect, session
import random
app = Flask(__name__)
app.secret_key="JADE"


@app.route('/')
def index():
	try:
		isinstance(session['serv_gold'],int)==True
	except:
		session['serv_gold']=0
	return render_template('index.html',gold=session['serv_gold'])

@app.route('/process', methods=['POST'])
def process():
	giver=request.form['building']
	if giver=="farm1":
		session['serv_gold']+=random.randrange(10, 21)
	elif giver=="cave1":
		session['serv_gold']+=random.randrange(5, 11)
	elif giver=="house1":
		session['serv_gold']+=random.randrange(2, 6)
	elif giver=="casino1":
		temp=random.randrange(0,2)
		if temp>0:
			session['serv_gold']+=random.randrange(0, 51)
		else:
			session['serv_gold']-=random.randrange(0, 51)	
	return redirect('/')


app.run(debug=True)