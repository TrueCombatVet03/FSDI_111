from flask import Flask         #from the flask module import the Flask Class.


app = Flask(__name__)           #create an instance of "Flask" into app.
                                # the "app" variable is also considered an object.

@app.get("/")                   # Flask decorator that allows us to map "/" to "index"
def index():                    # Python function - in Flask this is a "view Function"
    me = {                      # Python dictionary containing key-value pairs.
        "first_name": "Kevin",
        "last_name":  "Soldier",
        "hobbies": "Paintball",
        "active": True
    }

    return me                   #return statement. Flask converts dict to JSON.