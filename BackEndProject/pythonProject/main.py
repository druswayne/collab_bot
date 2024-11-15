from flask import Flask
import json

app = Flask(__name__)
with open('candidate.json', 'r', encoding='utf-8') as file:
    data = json.loads(file.read())
print(data)

@app.route("/")
def page_candidate():
    return "Candidate"

@app.route("/candidate/<uid>")
def page_index(uid):
    list_user = []
    for user in data:
        if user['id'] == uid:
            list_user.append(f"<pre> Имя кандидата - {user['name']} \n позиция кандидата - {user['position']} \n навыки через запятую - {user['skills']} \n </pre>")
            return ' '.join(list_user)

#def page_index():
#    list_user = []
#    for user in data:
#        list_user.append(f"<pre> Имя кандидата - {user['name']} \n позиция кандидата - {user['position']} \n навыки через запятую - {user['skills']} \n </pre>")
#    return ' '.join(list_user)

app.run(debug=True)