from flask import Flask
import os

app = Flask(__name__)
# Port number is required to fetch from env variable
# http://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#PORT


#cf_port = os.getenv("PORT")

# Only get method by default
@app.route('/')
def hello():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)