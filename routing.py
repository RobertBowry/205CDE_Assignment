from flask import Flask, make_response, abort, redirect, render_template
app = Flask(__name__);

@app.route('/')
def index():
    return render_template("Home_Page.html")

@app.route('/Portfolio')
def portfolio():
    return render_template("Portfolio_Page.html")
    
@app.route('/CV')
def cv():
    return render_template("CV_Page.html")

@app.route('/AboutMe')
def aboutme():
    return render_template("AboutMe_Page.html")

@app.route('/Contact')
def contactpage():
    return render_template("Contact_Page.html")
    
@app.route('/Form')
def formpage():
    return render_template("Form_Page.html")

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)