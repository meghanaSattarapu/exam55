from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def form():
    return render_template("form.html")
@app.route('/submit',method = 'POST')
def main():
    name = request.form['name']
    date = request.form['date']
    gender = request.form['gender']
    return render_template("greetings.html",name = name,date=date,gender = gender)
if(__name__=="__main__"):
    app.run(host = '0.0.0.0',port = 5000,debug = True)
