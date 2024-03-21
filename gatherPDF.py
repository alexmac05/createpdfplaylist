from flask import Flask
import requests


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
    # Define the URL you want to make a GET request to
    #url = 'https://api.github.com/'
    url = 'https://tabs.ultimate-guitar.com/tab/adrianne-lenker/angels-chords-3703085'
    # Make the GET request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the response content
        print(response.json())
    else:
        # If the request was not successful, print an error message
        print(f"Error: {response.status_code}")