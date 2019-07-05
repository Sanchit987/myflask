from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username':'sanchit'}
    posts = [{'a':{'username':'ashish'},'body':'What a Beautiful day'},{'a':{'username':'suraj'},'body':'excited to learn something new'}]
    return render_template('index.html',title = 'home',user = user,posts = posts)
    
