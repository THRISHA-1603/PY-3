from flask import Flask
import subprocess

# Create the Flask app
app = Flask(__name__)

# Define the API endpoint
@app.route('/api/printHello', methods=['GET'])
def print_hello():
    r = subprocess.check_output(['python','learngit.py'])
    return r.decode('utf-8')

# Run the Flask app 
if __name__ == '__main__':
    app.run()
