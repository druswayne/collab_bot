from flask import Flask, render_template, request
import json
app = Flask(__name__)
with open('candidate.json', 'r', encoding='utf-8') as file:
    data = json.loads(file.read())
print(data)

@app.route("/")
def page_index():
    return render_template('NewShab.html', name = data[i]["name"], position = data[i]["position"])

app.run()