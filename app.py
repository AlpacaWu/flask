from flask import Flask,render_template,url_for,redirect,request
app=Flask(__name__)
@app.route('/')
@app.route('/<name>')
def test(name=None):
    if name == None:
        return 'Hello World!'
    return 'Hello {} !'.format(name)
@app.route('/template')
def tem():
    return render_template('test.html')
@app.route('/redirect')
def red():
    return redirect(url_for('tem'))
@app.route('/request',methods=['POST','GET'])
def req():
	if request.method =='POST':
		if request.values['send']=='送出':
			return render_template('form.html',name=request.values['user'])
	return render_template('form.html',name="")
@app.route('/login')
def login():
    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)