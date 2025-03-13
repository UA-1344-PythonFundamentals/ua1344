from flask import Flask, url_for, request, render_template, redirect
from models import generate_users, User

app = Flask(__name__)

USERS = generate_users()

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


# @app.route("/user",  methods=['GET', 'POST'])
# def get_all_users():
#     if request.method == 'GET':
#         return [user.to_dict() for user in USERS]
#     elif request.method == "POST":
#         return "201 created"

# @app.route("/user/<int:pk>")
# def get_user_by_id(pk):
#     for user in USERS:
#         if user.pk == pk:
#             return user.to_dict()
#     return  []

@app.route("/user")
@app.route("/user/<int:pk>")
def get_user(pk=None):
    if pk:
        result = None
        for u in USERS:
            if u.pk == pk:
                result = u
        return render_template("user_info.html", user=result)
    else:
        return render_template("user_list.html", users=USERS)


@app.route("/user/create", methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return render_template("create_user.html")
    elif request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password'] #Hash this password
        full_name = request.form.get('full_name')

        new_user = User(username, email, password, full_name)
        USERS.append(new_user)
        return redirect(url_for('get_user')) #redirect back to form.

     


if __name__ == '__main__':
    # with app.test_request_context():
    #      print(url_for('hello_world'))
    #      print(url_for('get_all_users'))
    #      print(url_for('get_user_by_id', pk=15))
    app.run(host="0.0.0.0", port=3000)

