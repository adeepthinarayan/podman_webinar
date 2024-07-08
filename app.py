# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "What is Podman?",
        "options": [
            "A container engine",
            "A programming language",
            "A web framework"
        ],
        "answer": "A container engine"
    },
    {
        "question": "Which command is used to build an image in Podman?",
        "options": [
            "podman build",
            "podman create",
            "podman init"
        ],
        "answer": "podman build"
    }
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    selected_options = {}
    if request.method == "POST":
        for i, question in enumerate(questions):
            selected_option = request.form.get(f"question-{i}")
            selected_options[i] = selected_option
    return render_template("quiz.html", questions=questions, selected_options=selected_options)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
