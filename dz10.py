import json
from flask import Flask
import requests

with open('candidates.json') as file:
    raw_json = file.read()
    new_list = json.loads(raw_json)
#print(new_list)


app = Flask(__name__)

@app.route("/")
def page():
    person = """"""
    for i in new_list:
        name = i['name']
        position = i['position']
        skills = i['skills']
        person += f"""
        Имя кандидата: {name}
        Позиция: {position}
        Навыки: {skills}
        
        """

    return f'<pre>{person}</pre>'

@app.route('/candidates/<int:x>')
def candidate(x):
    person = """"""
    for i in range(len(new_list)):
        if i == (x - 1):
            name = new_list[i]['name']
            position = new_list[i]['position']
            skills = new_list[i]['skills']
            picture = new_list[i]['picture']
            person += f"""
            img src = {picture}
            Имя кандидата: {name}
            Позиция: {position}
            Навыки: {skills}

            """
    return f'<pre>{person}</pre>'

@app.route('/skills/<x>')
def skill(x):
    person = """"""
    for i in new_list:
        if x.lower() in i['skills'].lower():
            name = i['name']
            position = i['position']
            skills = i['skills']
            person += f"""
                    Имя кандидата: {name}
                    Позиция: {position}
                    Навыки: {skills}

                    """

    return f'<pre>{person}</pre>'


app.run()
