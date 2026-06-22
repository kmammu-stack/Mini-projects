from flask import Flask, render_template, request, redirect, url_value_preprocessor

app = Flask(__name__)

# In-memory list to store tasks since no database is used yet
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    if task:
        todos.append(task)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_todo(task_id):
    if 0 <= task_id < len(todos):
        todos.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)