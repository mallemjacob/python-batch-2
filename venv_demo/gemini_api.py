from google import genai
from flask import Flask

user_input  = input('Enter a question: ')

API_KEY = ""
client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=user_input
)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>" + response.text + "</p>"
