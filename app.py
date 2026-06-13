from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Our interactive learning roadmap data (Python Basics)
QUESTIONS = [
    {
        "id": 1,
        "question": "Which of the following is used to define a block of code in Python?",
        "options": ["Indentation", "Curly braces", "Parentheses", "Quotation marks"],
        "correct_index": 0
    },
    {
        "id": 2,
        "question": "What is the output of print(2 ** 3)?",
        "options": ["5", "6", "8", "9"],
        "correct_index": 2
    },
    {
        "id": 3,
        "question": "Which data type is immutable in Python?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "correct_index": 3
    },
    {
        "id": 4,
        "question": "How do you insert comments in Python code?",
        "options": ["// This is a comment", "/* This is a comment */", "# This is a comment", "-- This is a comment"],
        "correct_index": 2
    },
    {
        "id": 5,
        "question": "Which keyword is used to create a function in Python?",
        "options": ["function", "def", "create", "fun"],
        "correct_index": 1
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/questions', methods=['GET'])
def get_questions():
    # Send questions without the correct answers to the frontend
    secure_questions = [
        {"id": q["id"], "question": q["question"], "options": q["options"]} 
        for q in QUESTIONS
    ]
    return jsonify(secure_questions)

@app.route('/api/verify', methods=['POST'])
def verify_answer():
    data = request.json
    q_id = data.get('id')
    user_answer = data.get('answer_index')
    
    # Find the question and check the answer
    for q in QUESTIONS:
        if q['id'] == q_id:
            is_correct = (q['correct_index'] == user_answer)
            return jsonify({
                "correct": is_correct, 
                "correct_index": q['correct_index']
            })
            
    return jsonify({"error": "Question not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)