from flask import Flask, render_template
import random 
app = Flask(__name__)
 
 
@app.route('/')
def index():
    now = random.randint(0, 10)
    return render_template("base.html", status=now)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
