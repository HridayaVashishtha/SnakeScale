from flask import Flask, render_template, request, redirect, url_for
import random as r
from time import time

app = Flask(__name__)

# Sample texts for typing test
examples = [
    "Achieving a high level of typing proficiency involves a combination of regular practice, proper finger placement, and the gradual reduction of reliance on visual cues, all of which contribute to both speed and accuracy over time.",
    "To reach your typing goals, it's important to incorporate various exercises that challenge different aspects of your typing skills, such as typing long paragraphs, practicing with complex texts, and using typing tests to track your progress.",
    "Investing time in developing your typing technique can lead to significant improvements in your productivity, as faster and more accurate typing can streamline your work process and enhance overall efficiency in both professional and personal tasks."
]

def errors(og, userinput):
    count = 0
    for i in range(min(len(og), len(userinput))):
        if og[i] != userinput[i]:
            count += 1
    count += abs(len(og) - len(userinput))
    correct = len(og) - count
    accuracy = (correct / len(og)) * 100
    return accuracy

def timetaken(start, end, userinput):
    duration = round((end - start), 3) / 60
    word_count = len(userinput.split())
    return word_count / duration

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        test = request.form['test']
        start_time = float(request.form['start_time'])
        userinput = request.form['userinput']
        end_time = time()

        netspeed = timetaken(start_time, end_time, userinput)
        accuracy = errors(test, userinput)

        return render_template('result.html', speed=round(netspeed, 3), accuracy=round(accuracy, 2), test=test)
    
    test = r.choice(examples)
    start_time = time()
    return render_template('index.html', test=test, start_time=start_time)

if __name__ == '__main__':
    app.run(debug=True)
