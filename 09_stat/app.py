from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def letsGo():
    return render_template("foo.html",collection=[1,2,34,5])
if __name__=='__main__':
     app.run(degbug==True)
