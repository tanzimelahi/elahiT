from flask import Flask,render_template,redirect,url_for,request,session
app=Flask(__name__)
app.secret_key="hijibiji"
@app.route("/")
def login():
    if "username" in session:
        return render_template("welcome.html")
    else:
        return render_template("login.html")
@app.route("/login")
def auth():
      username=request.args["username"]
      password=request.args["password"]
      dictionary={'username':'Tanzim','password':'Elahi'}
      if username==dictionary['username'] and password==dictionary['password']:
          session['username']=username
          return render_template("welcome.html")
      else:

          return render_template("error.html")
@app.route("/error")
def err():
     return render_template("error.html")
@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("login"))
if __name__== "__main__":
    app.debug=True
    app.run()
