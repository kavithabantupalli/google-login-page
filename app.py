from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# @app.route("/home",methods=["GET"])---> endpoint.(error--not found)

@app.route("/",methods=["GET"])
def homepage():
    return "<h>Hello QIS!!!!!!!!</h>" 

'''@app.route("/home",methods=["GET"])
def frontend():
    return "Lumen" '''

@app.route("/home",methods=["GET"])
def frontend():
    return render_template("index.html")


database=[]
@app.route("/reg_data",methods=["POST"])
def get_reg_data():
    user={}
    name = request.form["u_name"]
    email = request.form["u_email"]
    phone = request.form["u_phone"]
    password = request.form["u_pwd"]
    print(name,email,phone,password)
    #return [name,email,phone,password] -----> to get json format data of user (entered)
    
    user["user_name"]=name
    user["user_email"]=email
    user["user_num"]=phone
    user["user_pwd"]=password

    database.append(user)
    return redirect("/home") #same page ki ravatkaniki




@app.route("/login",methods=["POST"])
def get_login_data():
    log_email = request.form["u_email"]
    log_password = request.form["u_pwd"]
    for user in range(len(database)):
        email = database[user]["user_email"]
        pwd = database[user]["user_pwd"]
        if log_email==email and log_password==pwd:
            return '''
                <div style="text-align:center; font-size:2em; margin-top:20px; animation: fadeIn 2s;">
                    <h1 style="color: green;">Logged in Successfully 😊</h1>
                </div>
                <style>
                    @keyframes fadeIn {
                        from { opacity: 0; transform: translateY(-20px); }
                        to { opacity: 1; transform: translateY(0); }
                    }
                </style>
            '''
        else:
            return "Invalid Credentials 😢"
    #print(email,password)
    return redirect('/home')

app.run(debug=True)

@app.route('/db',methods=["GET"])
def view_database():
    return database
