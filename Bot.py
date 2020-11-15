from flask import Flask ,request,redirect,url_for


app = Flask(__name__)
# Port number is required to fetch from env variable
# http://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#PORT

Json = "NULL"
#cf_port = os.getenv("PORT")

# Only get method by default
@app.route('/')
def hello():
    return 'Hello World'

@app.route("/Modify", methods = ["POST", "GET"])
def Modify():

    if request.method == "POST":
        JSON = "It Worked"
        return redirect(url_for("Modify_Return", Json = JSON))
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