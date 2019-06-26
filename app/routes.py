from app import app
@app.route('/')
@app.route('/index')
def index():
    #return "Hello , world"
    user = {'username':'sanchit'}
    return '''
    <html>
    <head>
    <title>Home page - microblog </title>
    </head>
    <body bgcolor = 'cyan'>
    <h1> hello , ''' + user['username'] + '''</h1>
    </body>
    </html>'''
