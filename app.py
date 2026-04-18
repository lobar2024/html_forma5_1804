from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        number = request.form.get('age')

        return render_template('result5.html', email=email, number=number)

    return render_template('index4.html')

if __name__ == '__main__':
    app.run(debug=True)
