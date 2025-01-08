from flask import Flask, render_template, jsonify,request, redirect, url_for

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
    return render_template('home.html')
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS) 


# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        # Example: Add logic for authentication here (e.g., check credentials)
        if email and password:  # Replace this with real validation
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

# Dashboard Route
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", jobs=JOBS)

@app.route("/add")
def add():
    return render_template("addingData.html")

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)