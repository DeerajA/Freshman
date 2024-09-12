from flask import Blueprint, render_template, request, redirect, url_for
views = Blueprint(__name__, "views")

tasks = []

@views.route("/")
def home():
    return render_template("index.html", tasks = tasks)

@views.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@views.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('views.index'))

@views.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('views.index'))
