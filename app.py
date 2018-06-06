from flask import Flask, flash, redirect, render_template, request, session, abort
import trackingmore
import pprint
p = pprint.PrettyPrinter()

app = Flask(__name__)
 
@app.route("/")
def index():
    trackingmore.set_api_key('fbbf2fc8-176b-4e23-aaec-8dac6e110150')
    print("lll")
    var1 = trackingmore.create_tracking_data('delhivery','379211877610')
    print("")
    s = trackingmore.realtime_tracking(var1)
    print("lll")
    return render_template('test.html',**locals())
 
@app.route('/login')
def home():
    return render_template('login.html')
    
@app.route("/members")
def members():
    return "Members"
 
@app.route("/members/<string:name>/")
def getMember(name):
    return render_template('test.html',name=name)
 
if __name__ == "__main__":
    app.run()
