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
        "question": "Which company develops Podman?",
        "options": [
            "Red Hat",
            "Google",
            "Microsoft"
        ],
        "answer": "Red Hat"
    },
    {
        "question": "Can Podman run containers without requiring a daemon?",
        "options": [
            "Yes",
            "No",
            "Only in certain configurations",
            "It depends on the operating system"
        ],
        "answer": "Yes"
    },
    {
        "question": "How do you pull an image from a container registry in Podman?",
        "options": [
            "podman image fetch",
            "podman image pull",
            "podman image get",
            "podman image download"
        ],
        "answer": "podman image pull"
    },
    {
        "question": "Which option allows you to run a container in the background?",
        "options": [
            "-d",
            "-t",
            "-i",
            "-p"
        ],
        "answer": "-d"
    }
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    selected_options = {}
    if request.method == "POST":
        for i, question in enumerate(questions):
            selected_option = request.form.get(f"question-{i}")
            selected_options[i] = selected_option
    return render_template("quiz.html", questions=questions, selected_options=selected_options, enumerate=enumerate)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
