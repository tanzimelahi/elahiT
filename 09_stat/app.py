from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def foo():
	return "hello"

@app.route("/template")
def letsGo():
    return render_template("foo.html",foo='foooo',collection=[1,2,34,5])
if __name__=='__main__':
	app.debug = True
	app.run()
