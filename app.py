

from flask import Flask,redirect,render_template,request

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")



@app.route("/",methods=["POST"])
def you():
	if request.method == 'POST':
		if request.form['submit_button'] == 'youtube':
			text=request.form['query']
			text=text.replace(' ','+')
			return redirect("https://www.youtube.com/results?search_query="+text) 
		elif request.form['submit_button'] == 'google':
			text=request.form['query']			
			text=text.replace(' ','+')
			return redirect("https://www.google.com/search?q="+text)
		elif request.form['submit_button'] == 'amazon':
			text=request.form['query']			
			text=text.replace(' ','+')
			return redirect("https://www.amazon.in/s?k="+text)
		else:
			return "404 error"
	elif request.method == 'GET':
		return render_template('index.html')
	


if __name__=="__main__":
	app.run()


