from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'FIXME'

@app.route('/greeting', methods=['GET'])
def greeting():
    # message = 'FIXME'
    # name = 'FIXME'
    return 'FIXME'

if __name__ == '__main__':
    app.run(debug=True)

''' 
If you have finished this lab you can go to the command line and type

    python labs/webapp.py

This will start the web application. 
You can then visit http://localhost:5000/ in your web browser to see the home page.
If you go to  http://localhost:5000/greeting?message=Hi&name=Alice to see the greeting page with a custom message and name.
'''