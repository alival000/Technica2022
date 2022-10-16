from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

'''
    {question number: [question number, question, [answer1, answer2, etc.]]}
'''
questions_answers = {
    1: [1, "Which one of Zac Efron's eyes do you feel in your soul?", [["1", "q1a.png"], ["2", "q1b.png"], ["3", "q1c.png"]]],
    2: [2, "Which Vanessa Hudgens' outfit can you see yourself wearing in the halls of East High?",
        [["1", "q2a.png"], ["2", "q2b.png"] , ["3", "q2c.png"]]],
    3: [3, "How would you describe your style?",
        [["1", "You are into the classics and have a timeless look"], ["2", "You like to be different and stand out"],
         ["3", "You go for a more mature and refined look"]]],
    4: [4, "What song makes you want to get up on stage and sing your heart out?", [["1", "q4a.mp3"], ["2", "q4b.mp3"], ["3", "q4c.mp3"]]],
    5: [5, "It's Friday Night and you are in your feels, what's going on?",
        [["1", "Your situationship has been talking smack behind your back"],
         ["2", "Your boyfriend has been getting a little too close to the girl you 'don't have to worry about'"],
         ["3", "You are starting a long distance relationship soon"]]],
    6: [6, "Which location sounds like a dream vacation?",
        [["1", "Mountainside cabin"], ["2", "Desert getaway"], ["3", "California beach day"]]],
    7: [7, "What kind of song would you want Julliard Scholar Kelsi Nielson to write you?",
        [["1", "Inspirational ballad"], ["2", "Upbeat duet"], ["3", "Confession of love"]]],
    8: [8, "Pick a Kardashian", [["1", "q8a,png"], ["2", "q8b.png"], ["3", "q8c.png"]]],
    9: [9, "Which quote ~inspires~ you?",
        [["1", "I come with my own background music"], ["2", "I majored in vacation"], ["3", "Worship Waffles"]]],
    10: [10, "What moment did you look forward to all of high school?",
         [["1", "Friday night football"], ["2", "Summer vacation"], ["3", "Prom"]]]
}

results = {
    1: 0,
    2: 0,
    3: 0
}

@app.route("/")
def root():
    return "Welcome to the High School Musical Personality Quiz!"


@app.route("/questions/<question_number>")
def questions(question_number):
    return render_template("questions.html", data = questions_answers[int(question_number)]);

@app.route("/NextQuestion/<question_number>", methods=["GET", "POST"])
def question_counter(question_number):
    answer = request.form['answer'];
    results[int(answer)] += 1
    next_question_number = int(question_number) + 1
    print(results)
    return redirect(url_for('questions', question_number = next_question_number))


if __name__ == '__main__':
   app.run()
