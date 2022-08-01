from flask import Flask, request, render_template, redirect, url_for, abort
from models import todos

from forms import TodoForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret_key"


@app.route("/", methods=["GET", "POST"])
@app.route("/todos/", methods=["GET", "POST"])
def todos_list():
    form = TodoForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            todos.create(form.data)
            todos.save_all()
        return redirect(url_for("todos_list"))

    return render_template("todos.html", form=form, todos=todos.all(), error=error)


@app.route("/todos/<int:todo_id>/", methods=["GET", "POST"])
def todo_details(todo_id):
    todo = todos.get(todo_id - 1)
    form = TodoForm(data=todo)

    if request.method == "POST":
        if form.validate_on_submit():
            todos.update(todo_id - 1, form.data)
        return redirect(url_for("todos_list"))
    return render_template("todo_id.html", form=form, todo_id=todo_id)


@app.route("/delete/<int:todo_id>/", methods=["GET", "DELETE"])
def delete_todo(todo_id):
    todo = todos.delete(todo_id - 1)
    todos.save_all()
    if not todo:
        abort(404)

    return redirect(url_for("todos_list"))


if __name__ == "__main__":
    app.run(debug=True)