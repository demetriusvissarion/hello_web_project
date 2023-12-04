import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# Request:
# GET /hello?name=David
@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'
    # Send back a friendly greeting with the name
    return f"Hello {name}!"

# Request:
# POST /goodbye
#   With body parameter: name=Alice
@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'
    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

# Request:
# POST /submit
#   With body parameter: name=Leo and message=Hello world
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name'] 
    message = request.form['message'] 
    # Send back a reply
    return f'Thanks {name}, you sent this message: "{message}"'
# curl -X POST -d "name=Leo&message=Hello World" http://localhost:5001/submit


# Request:
# GET /wave
#   With body parameter: name=John
@app.route('/wave', methods=['GET'])
def wave():
    # name = request.form['name'] 
    name = request.args['name']
    # Send back a reply
    return f"I am waving at {name}"
# curl -X POST -d "name=John" http://localhost:5001/wave


# Request:
# POST /count_vowels
#   With body parameter: text=eee
@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    # Send back number of vowels in the text
    num_vowels=0
    for char in text:
        if char in "aeiouAEIOU":
            num_vowels = num_vowels+1
    return f'There are {num_vowels} vowels in "{text}"'
# curl -X POST -d "text=eee" http://localhost:5001/count_vowels


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

