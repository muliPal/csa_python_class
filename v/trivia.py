from IPython.display import display, HTML
import random
from turtle import Screen, Turtle
import time

# ----------------------------
# Participants and Instructors
# ----------------------------
participants = ["Benard", "June", "Aisha", "Kevin", "Zuri", "James", "Fatima", "David"]
instructors = ["Alice", "Brian", "Cynthia", "Daniel"]

# ----------------------------
# Questions and Answers
# ----------------------------
questions = {
    "easy": [
        "Who founded CSA?",
        "When was CSA founded?",
        "How many camps have been held?",
        "First country where a CSA camp was held?",
        "Which language is used for coding in CSA?"
    ],
    "medium": [
        "Name 3 tutors in the current camp.",
        "Name three countries impacted by CSA.",
        "Where is Glasgow?",
        "How many countries has CSA impacted?",
        "Which years didn’t have a CSA camp?"
    ],
    "hard": [
        "Who was president where the first CSA workshop was held?",
        "What was the theme of the 2022 Women’s Conference?",
        "Which institution has CSA partnered with in Rwanda?",
        "What % of women applied in 2022?",
        "Who is quoted in 2018 workshop testimonials?"
    ]
}

structured_answers = {
    'Easy': {
        'Who founded CSA?': 'Dr.Sofiat Olaosebikan',
        'When was CSA founded?': '2018',
        'How many camps have been held?': '5',
        'First country where a CSA camp was held?': 'Nigeria',
        'Which language is used for coding in CSA?': 'Python'
    },
    'Medium': {
        'Name 3 tutors in the current camp.': 'Fionnuala Johnson, Kenechie Omeke, Stephen McQuistin',
        'Name three countries impacted by CSA.': 'Kenya, Nigeria, Rwanda',
        'Where is Glasgow?': 'Scotland',
        'How many countries has CSA impacted?': '12',
        'Which years didn’t have a CSA camp?': '2020, 2023, 2024'
    },
    'Hard': {
        'Who was president where the first CSA workshop was held?': 'Muhammadu Buhari',
        'What was the theme of the 2022 Women’s Conference?': 'Breaking the Glass Ceiling',
        'Which institution has CSA partnered with in Rwanda?': 'University of Rwanda',
        'What % of women applied in 2022?': '47%',
        'Who is quoted in 2018 workshop testimonials?': 'Deborah Oluwabunmi Joseph'
    }
}

points = {
    "easy": 1,
    "medium": 2,
    "hard": 3
}

# ----------------------------
# Flag Drawing Function
# ----------------------------
def draw_flag():
    screen = Screen()
    screen.title("CSA Legacy Flag")
    t = Turtle()
    t.speed(3)

    # Draw a blue rectangle
    t.penup()
    t.goto(-100, 50)
    t.pendown()
    t.color("blue", "skyblue")
    t.begin_fill()
    for _ in range(2):
        t.forward(200)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()

    # Draw a white star (symbolic)
    t.penup()
    t.goto(-20, -10)
    t.color("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(40)
        t.right(144)
    t.end_fill()

    time.sleep(4)
    screen.bye()

# ----------------------------
# Ask and Process Question
# ----------------------------
def ask_question(level, player_name):
    level_cap = level.capitalize()
    all_questions = questions[level]
    selected_question = random.choice(all_questions)
    correct_answer = structured_answers[level_cap][selected_question]

    display(HTML(f"""
        <div style='border:2px solid #333; padding:15px; margin:10px 0; background:#f0f8ff;'>
            <h3 style='color:#2a52be;'>🧠 {player_name}, your <u>{level.upper()}</u> question is:</h3>
            <p style='font-size:18px;'>👉 <strong>{selected_question}</strong></p>
        </div>
    """))

    user_answer = input("Your answer: ").strip()

    if user_answer.lower() == correct_answer.lower():
        display(HTML("<p style='color:green; font-weight:bold;'>✅ Correct!</p>"))
        score = points[level]
    else:
        display(HTML(f"<p style='color:red; font-weight:bold;'>❌ Incorrect. The correct answer is: <em>{correct_answer}</em></p>"))
        score = 0

    # Show fun facts
    facts_html = "<ul>"
    for q in all_questions:
        if q != selected_question:
            facts_html += f"<li><strong>{q}</strong> → {structured_answers[level_cap][q]}</li>"
    facts_html += "</ul>"

    display(HTML(f"""
        <div style='margin-top:10px; background:#e6f7ff; padding:10px; border-left:5px solid #2a52be;'>
            <h4>🎉 Fun Facts from this level:</h4>
            {facts_html}
        </div>
    """))

    # Draw flag if hard
    if level == "hard":
        display(HTML("<h3 style='color:blue;'>🚩 Drawing the CSA Legacy Flag...</h3>"))
        draw_flag()

    return score

# ----------------------------
# Run the Game
# ----------------------------
total_score = 0

easy_player = random.choice(participants)
total_score += ask_question('easy', easy_player)

medium_player = input("\n🙋 Who is volunteering to answer the MEDIUM question? Enter your name: ").strip()
total_score += ask_question('medium', medium_player)

hard_player = random.choice(instructors)
total_score += ask_question('hard', hard_player)

display(HTML(f"""
    <div style='margin-top:20px; padding:15px; background:#d1ffd1; border:2px solid green;'>
        <h2>🏁 Total score this round: {total_score} points</h2>
    </div>
"""))
