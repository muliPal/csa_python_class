from IPython.display import display, HTML
import random
from turtle import Screen, Turtle
import time

# ----------------------------
# Participants and Instructors
# ----------------------------
# Import the list from participants.txt
# ----------------------------
# Questions and Answers
# ----------------------------
# Import from questions.txt
points = {
    "easy": 1,
    "medium": 2,
    "hard": 3
}

# ----------------------------
# Flag Drawing Function
# ----------------------------
# Figure out how to call the flag drawing class

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
