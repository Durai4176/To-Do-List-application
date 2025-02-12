from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")  # Ensure templates folder is set correctly

tasks = []

@app.route('/')
def home():
    try:
        return render_template('index.html', tasks=tasks)
    except:
        return "<h1>Error: index.html not found in the templates folder!</h1>", 500

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)


