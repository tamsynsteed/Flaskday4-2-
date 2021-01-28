from flask import Flask,render_template,url_for,redirect

app=Flask(__name__)

@app.route('/index/<user>')
def index(user):
    return render_template('greet.html',name=user)

@app.route('/Grading/<int:score>')
def grades(score):
    return render_template('grade.html', grade=score)

@app.route('/register')
def register():
    names={'chelsea:laguma','Odwa:Nodada','zoe:engel'}
    return render_template('myregister.html', register=names)

if __name__=='__main__':
    app.run(debug=True)
