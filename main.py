from pyscript import document
import random

all_challenges = [
    {"text": "'You're just a kid, so your opinion on climate change doesn't matter!'", "options": ["Ad Hominem", "Slippery Slope", "Straw Man", "Hasty Generalization"], "correct": "Ad Hominem", "explanation": "Correct! This attacks the person rather than the argument."},
    {"text": "'If we let students use calculators, eventually society will collapse!'", "options": ["Circular Logic", "Slippery Slope", "Ad Hominem", "False Dilemma"], "correct": "Slippery Slope", "explanation": "Correct! This assumes a chain reaction without proof."},
    {"text": "'My grandfather smoked and lived to 90, so smoking is fine.'", "options": ["Hasty Generalization", "Straw Man", "Ad Hominem", "Red Herring"], "correct": "Hasty Generalization", "explanation": "Correct! Drawing a broad conclusion from one example."},
    {"text": "'Either you support this law, or you hate our country!'", "options": ["False Dilemma", "Slippery Slope", "Circular Reasoning", "Ad Hominem"], "correct": "False Dilemma", "explanation": "Correct! This ignores the middle ground."},
    {"text": "'Senator Jones wants to fund schools. Why does he want to leave us defenseless?'", "options": ["Straw Man", "Red Herring", "Ad Hominem", "False Cause"], "correct": "Straw Man", "explanation": "Correct! Misrepresenting an argument to attack it easily."},
    {"text": "'I forgot my chores, but look at how hard I worked on my art project!'", "options": ["Red Herring", "Circular Logic", "Hasty Generalization", "Slippery Slope"], "correct": "Red Herring", "explanation": "Correct! Diverting attention to an irrelevant topic."},
    {"text": "'The book is a bestseller because everyone is buying it.'", "options": ["Circular Reasoning", "Ad Hominem", "False Cause", "Straw Man"], "correct": "Circular Reasoning", "explanation": "Correct! The argument repeats itself."},
    {"text": "'All humans are mortal. Socrates is human. Therefore, Socrates is mortal.'", "options": ["Categorical Logic", "Ad Hominem", "False Dilemma", "Red Herring"], "correct": "Categorical Logic", "explanation": "Correct! This is a valid Syllogism (Categorical Logic)."},
    {"text": "'I wore my lucky socks and we won. Therefore, the socks caused the win.'", "options": ["False Cause", "Straw Man", "Circular Logic", "Ad Hominem"], "correct": "False Cause", "explanation": "Correct! Correlation does not mean causation."},
    {"text": "'Everyone is doing this new TikTok challenge, so it must be safe.'", "options": ["Bandwagon", "Slippery Slope", "Straw Man", "False Cause"], "correct": "Bandwagon", "explanation": "Correct! Arguing something is right because it's popular."},
    {"text": "'A: We should be nicer to animals. B: Why do you want to shut down all farms?'", "options": ["Straw Man", "Red Herring", "Bandwagon", "Hasty Generalization"], "correct": "Straw Man", "explanation": "Correct! B distorted A's position."},
    {"text": "'You can't prove ghosts don't exist, so they must be real.'", "options": ["Appeal to Ignorance", "Ad Hominem", "False Dilemma", "Circular Logic"], "correct": "Appeal to Ignorance", "explanation": "Correct! Lack of evidence is not proof of the opposite."},
    {"text": "'No true Scotsman would ever put sugar on his porridge.'", "options": ["No True Scotsman", "Bandwagon", "False Cause", "Slippery Slope"], "correct": "No True Scotsman", "explanation": "Correct! Altering a definition to protect a universal claim."},
    {"text": "'If we allow one person to skip the line, everyone will start skipping!'", "options": ["Slippery Slope", "Straw Man", "Red Herring", "Ad Hominem"], "correct": "Slippery Slope", "explanation": "Correct! Predicting a drastic outcome from one event."},
    {"text": "'Drinking water is good because the body needs hydration to live.'", "options": ["Logical Statement", "Straw Man", "False Cause", "Ad Hominem"], "correct": "Logical Statement", "explanation": "Correct! This is a sound, fundamental logical premise."}
]

MAX_SCORE = 15
score = 0
game_deck = list(all_challenges)
random.shuffle(game_deck)

def load_challenge():
    global score
    
    if not game_deck or score >= MAX_SCORE:
        finish_game()
        return


    challenge = game_deck[-1]
    document.getElementById("scenario").innerText = challenge["text"]
    
    display_options = list(challenge["options"])
    random.shuffle(display_options)
    
    for i in range(4):
        btn = document.getElementById(f"opt{i}")
        btn.innerText = display_options[i]
        btn.value = display_options[i]
        btn.style.display = "block"

def finish_game():
    final_msg = "PERFECT SCORE!" if score == 15 else "GAME OVER"
    document.getElementById("scenario").innerHTML = f"<h2>{final_msg}</h2><p>You mastered {score}/15 logic challenges!</p>"
    for i in range(4):
        document.getElementById(f"opt{i}").style.display = "none"

def check_answer(event):
    global score
    
    challenge = game_deck.pop() 
    selected = event.target.value
    feedback_div = document.getElementById("feedback")
    
    if selected == challenge["correct"]:
        score += 1
        feedback_div.style.color = "#27ae60"
        feedback_div.innerText = challenge["explanation"]
    else:
        feedback_div.style.color = "#c0392b"
        feedback_div.innerText = f"Incorrect. That was: {challenge['correct']}"

    document.getElementById("score").innerText = str(score)
    load_challenge()

document.getElementById("max-score").innerText = str(MAX_SCORE)
load_challenge()