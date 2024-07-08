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
    },
    {
        "question": "How do you list all containers in Podman?",
        "options": [
            "podman ps",
            "podman list",
            "podman containers"
        ],
        "answer": "podman ps"
    },
    {
        "question": "Which command is used to remove a container in Podman?",
        "options": [
            "podman rm",
            "podman delete",
            "podman remove"
        ],
        "answer": "podman rm"
    },
    {
        "question": "How do you run a container in the background in Podman?",
        "options": [
            "podman run -d",
            "podman run -b",
            "podman run --background"
        ],
        "answer": "podman run -d"
    },
    {
        "question": "What is the default network mode for Podman containers?",
        "options": [
            "bridge",
            "host",
            "none"
        ],
        "answer": "bridge"
    },
    {
        "question": "How do you inspect the details of an image in Podman?",
        "options": [
            "podman inspect",
            "podman details",
            "podman info"
        ],
        "answer": "podman inspect"
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
