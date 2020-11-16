from flask import Flask ,request,redirect,url_for, jsonify
import json

app = Flask(__name__)
# Port number is required to fetch from env variable
# http://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#PORT

Json = "NULL"
#cf_port = os.getenv("PORT")

#pull credentials for database externally
def read_file():
    #This is the file location for my database information. Replace with your database information.
    #File location '../database_folder/database.txt'
    with open('../database_folder/database.txt', 'r') as f:
        f_content = f.read()
        f_content = f_content.split()

        username = f_content[0]
        password = f_content[1]

        return username, password


# Only get method by default
@app.route('/')
def hello():
    return 'Hello World'

@app.route("/Modify", methods = ["POST", "GET"])
def Modify():

    if request.method == "POST":

        value = request.json
        #Brackets t specify an object in an object example: request.json['Object']

        # Converts to Json
        json_str = json.dumps(value)

        #converts to a dictionary
        value = json.loads(json_str)
        JSON = value

        #Test file system
        username, password = read_file()

        #Test output for further modification
        output = {
            "input" : json.dumps(value),
            "postrgres_login" : {
                "Username": username,
                "Password": password}

         }

        output = json.dumps(output)

        return output         #value['Stores']['Target']

        #value['Stores']['Target'] ----> cheks the object stores for value Target

        #return redirect(url_for("Modify_Return", Json = JSON))
    else:
        if Json == "NULL":
            return redirect(url_for("Modify_Return", Json = "Json is null"))
        else:
            return redirect(url_for("Modify_Return", Json = JSON))

@app.route("/<Json>")
def Modify_Return(Json):
    return Json

if __name__ == "__main__":
     app.run(host='0.0.0.0',port=8080,debug=True)
# app.run(debug=True)