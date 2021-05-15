# flask server and webapp
# add a page to the webapp by creating a new route
# in a web application, a route is a certain path into your website, determined by the URL
# create the routes and determine what each route does



from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # this determines the entry point: / means the root f the website
def index(): #this is the name you gave to the route, index in this case for the index or homepage of the website
    return render_template('index.html') # this code makes Flask look for index.html in the templates directory that the app.py program is in
    return 'Hello World' # this is the  content of the web page, which is returned hen the user goes to the URL

@app.route('/family')
def family():
    return render_template('family.html')
    return 'I Love You!'

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

# this code runs the we bserver and the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # the host='0.0.0.0' means the web app is accessible to any device on the network

