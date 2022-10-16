from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

'''
    {question number: [question number, question, [answer1, answer2, etc.], ifImg]}
'''
questions_answers = {
    1: [1, "Which one of Zac Efron's eyes do you feel in your soul?",
        [["1", "q1a.jpg"], ["2", "q1b.jpg"], ["3", "q1c.jpg"]], True],
    2: [2, "Which Vanessa Hudgens' outfit can you see yourself wearing in the halls of East High?",
        [["1", "q2a.jpg"], ["2", "q2b.jpg"], ["3", "q2c.jpg"]], True],
    3: [3, "How would you describe your style?",
        [["1", "You are into the classics and have a timeless look"], ["2", "You like to be different and stand out"],
         ["3", "You go for a more mature and refined look"]], False],
    4: [4, "What song makes you want to get up on stage and sing your heart out?",
        [["1", "q4a.mp3"], ["2", "q4b.mp3"], ["3", "q4c.mp3"]], True],
    5: [5, "It's Friday Night and you are in your feels, what's going on?",
        [["1", "Your situationship has been talking smack behind your back"],
         ["2", "Your boyfriend has been getting a little too close to the girl you 'don't have to worry about'"],
         ["3", "You are starting a long distance relationship soon"]], False],
    6: [6, "Which location sounds like a dream vacation?",
        [["1", "Mountainside cabin"], ["2", "Desert getaway"], ["3", "California beach day"]], False],
    7: [7, "What kind of song would you want Julliard Scholar Kelsi Nielson to write you?",
<<<<<<< HEAD
        [["1", "Inspirational ballad"], ["2", "Upbeat duet"], ["3", "Confession of love"]], False],
    8: [8, "Pick a Kardashian/Jenner", [["1", "q8a,png"], ["2", "q8b.png"], ["3", "q8c.png"]], True],
=======
        [["1", "Inspirational ballad"], ["2", "Upbeat duet"], ["3", "Confession of love"]]],
    8: [8, "Pick a Kardashian", [["1", "q8a.jpg"], ["2", "q8b.jpg"], ["3", "q8c.jpg"]]],
>>>>>>> 1bd3d2ffb6ff2d12e94df67c076232d0728be8f6
    9: [9, "Which quote ~inspires~ you?",
        [["1", "I come with my own background music"], ["2", "I majored in vacation"], ["3", "Worship Waffles"]], False],
    10: [10, "What moment did you look forward to all of high school?",
         [["1", "Friday night football"], ["2", "Summer vacation"], ["3", "Prom"]], False]
}

results = {
    1: 0,
    2: 0,
    3: 0
}


@app.route("/")
def root():
    return render_template("page1.html")


@app.route("/questions/<question_number>")
def questions(question_number):
    random.shuffle(questions_answers[int(question_number)][2])
    return render_template("questions.html", data=questions_answers[int(question_number)]);


@app.route("/results")
def quiz_results():
    hsm1 = results[1]
    hsm2 = results[2]
    hsm3 = results[3]

    if hsm1 > hsm2 and hsm1 > hsm3:
        return "hsm1 " + str(hsm1), 200
    elif hsm2 > hsm1 and hsm2 > hsm3:
        return "hsm2 " + str(hsm2), 200
    else:
        return "hsm3 "+ str(hsm3), 200


@app.route("/NextQuestion/<question_number>", methods=["GET", "POST"])
def question_counter(question_number):
    answer = request.form['answer'];
    results[int(answer)] += 1
    next_question_number = int(question_number) + 1
    if next_question_number <= 10:
        return redirect(url_for('questions', question_number=next_question_number))
    else:
        return redirect(url_for('quiz_results'))


@app.route("/FirstQuestion", methods=["GET", "POST"])
def first_question():
    return redirect(url_for('questions', question_number=1))


if __name__ == '__main__':
    app.run()
