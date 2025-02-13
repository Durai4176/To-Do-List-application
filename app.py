import os
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>To-Do List</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #ff9a9e, #fad0c4);
                color: #333;
                text-align: center;
                padding: 20px;
            }}

            .container {{
                max-width: 400px;
                margin: 50px auto;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            }}

            h1 {{
                color: #444;
            }}

            form {{
                margin-bottom: 20px;
            }}

            input {{
                width: 80%;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                outline: none;
            }}

            button {{
                padding: 10px;
                border: none;
                background: #ff6b81;
                color: white;
                border-radius: 5px;
                cursor: pointer;
            }}

            button:hover {{
                background: #ff4757;
            }}

            ul {{
                list-style: none;
                padding: 0;
            }}

            li {{
                background: #f8f8f8;
                padding: 10px;
                margin: 5px 0;
                border-radius: 5px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}

            .delete-btn {{
                text-decoration: none;
                background: #ff4757;
                color: white;
                padding: 5px 10px;
                border-radius: 5px;
            }}

            .delete-btn:hover {{
                background: #e84118;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📝 To-Do List</h1>

            <form action="/add" method="POST">
                <input type="text" name="task" placeholder="Enter a new task" required>
                <button type="submit">Add Task</button>
            </form>

            <ul>
                {"".join([f'<li>{task} <a href="/delete/{i}" class="delete-btn">❌</a></li>' for i, task in enumerate(tasks)])}
            </ul>
        </div>
    </body>
    </html>
    """

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
    port = int(os.environ.get('PORT', 5000))  # Use Render's PORT or default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)
