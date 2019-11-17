#%%
# import flask
# app = flask.Flask(__name__)
# app.config['DEBUG'] = True

# @app.route('/',methods=['GET'])
# def home():
#     return "<h1>Welcome to our website</h1><p>This site is a prototype for GreyAtom made by jibran khan"

# app.run(host = '127.0.0.1' , port = '5100')

    
# %%
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

employee = [
    {'Name': "Puneet Jain",
    'Id': 1,
     'Designation': 'Mentor',
     'joined': '2018'},
    {'Name': "Nipun Narang",
     'Id': 2,
     'Designation': 'Student',
     'joined': '2019'},
    {'Name': "Amit Kumar",
     'Id': 3,
     'Designation': 'Operation Head',
     'joined': '2017'}
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to our website</h1><p>This site is a prototype API for GreyAtom.</p>"

@app.route('/api/v1/resources/employee/all', methods=['GET'])
def api_all():
    return jsonify(employee)


@app.route('/api/v1/resources/employee/', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'Id' in request.args:
        id = int(request.args['Id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for employ in employee:

        if employ['Id'] == id:
            results.append(employ)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()

app.run(host='0.0.0.0', port=5000)
