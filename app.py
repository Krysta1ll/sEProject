from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("sysLoginPage.html")


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        print("success")
        result = request.form
        return render_template("success.html", result=result)
    else:
        print("error")


@app.route('/success')
def login():
    print("重定向成功")
    return 'success'


if __name__ == '__main__':
    app.run()
