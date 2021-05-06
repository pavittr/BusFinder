from flask import Flask
import requests



app = Flask(__name__)



@app.route('/')
def index():

    postcode_url = "https://postcodes.io/"
    r = requests.post('https://api.postcodes.io/postcodes', {'postcodes' : ["NW5 1TL"]})
    print(r.json())

    return 'Hello World!'


if __name__ == '__main__':
    app.run()