import json

def getQuizData():
    with open('data/quiz.json', 'r') as file:
        data = json.load(file)

    return print(data)

getQuizData()