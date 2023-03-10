from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("loginView.html")


@app.route('/login', methods=['POST', 'GET'])
def login_index():
    if request.method == 'POST':

        print("success")
        return redirect(url_for('login'))
    else:
        print("error")


@app.route('/success')
def login():
    print("重定向成功")
    return 'success'


if __name__ == '__main__':
    app.run()
