from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/', methods=['GET','POST'])
def hello_world():
    return 'Hello, World! I will make some changes.'

# Run the Flask app if this script is executed
if __name__ == '__main__':
    app.run()
