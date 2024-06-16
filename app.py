from flask import Flask, render_template, request, session
import urllib.request
import json
import os 
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Fetch environment variables
ENDPOINT_URL = os.getenv("ENDPOINT_URL")
API_KEY = os.getenv("API_KEY")

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed to use sessions

@app.route('/', methods=['POST', 'GET'])
def handle_form():
    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        # Handle POST request
        query = request.form.get('user-input')  # Get user input from form
        
        # Prepare data to be sent to the endpoint
        data = {"query": query}
        body = json.dumps(data).encode('utf-8')  # Encode data as JSON

        if not API_KEY:
            raise Exception("A key should be provided to invoke the endpoint")

        # Headers for the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + API_KEY,
            'azureml-model-deployment': 'rag-app-neo4j-1'
        }

        # Create a request object
        req = urllib.request.Request(ENDPOINT_URL, body, headers)

        try:
            # Make the request to the endpoint
            response = urllib.request.urlopen(req)

            # Read and decode the response
            result = response.read()
            result_json = json.loads(result.decode('utf-8'))
            reply = result_json.get('reply', '')  # Extract reply from JSON response
            
            # Save the conversation in session
            session['history'].append({'user': query, 'bot': reply})
            session.modified = True
            
            # Render the template with the conversation history
            return render_template('chatbot.html', history=session['history'])
        
        except urllib.error.HTTPError as error:
            # Handle HTTP errors
            print("The request failed with status code: " + str(error.code))
            print(error.info())
            print(error.read().decode("utf8", 'ignore'))
    
    else:
        # Handle GET request
        return render_template('chatbot.html', history=session['history'])

if __name__ == '__main__':
    app.run()
