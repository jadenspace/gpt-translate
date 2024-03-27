from flask import Flask, request, render_template
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
app = Flask(__name__)

@app.route("/translater", methods=["post"])
def translater():
    data = request.json

    language = data["language"]
    text = data["text"]

    prompt = f"Translate the sentences below to the following {language}\n\n{text}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "you are a translater."
            },
            {
                "role": "system",
                "content": "Please express only the translated text concisely."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

@app.route("/web")
def web():
    return render_template("index.html")

@app.route("/")
def index():
    return "Hello World"

app.run(host="0.0.0.0", port=81)
