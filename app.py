from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS =[
    {
        'id':1,
        'totalIncome': '100',
        'totalExpenses': '50',
        'totalBalance': '50',
        'expensesBar':'50',
        'category': 'Food',
        'amount':'10',
        'notes': 'groceries'
        
    }
]
@app.route("/")
def hello_world():
    return render_template('dashboard.html',
                          jobs=JOBS)
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS) 
if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)