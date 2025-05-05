from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        # Extract values from form
        a11 = int(request.form['a11'])
        a12 = int(request.form['a12'])
        a21 = int(request.form['a21'])
        a22 = int(request.form['a22'])

        b11 = int(request.form['b11'])
        b12 = int(request.form['b12'])
        b21 = int(request.form['b21'])
        b22 = int(request.form['b22'])

        # Matrix multiplication (2x2)
        result = [
            [a11*b11 + a12*b21, a11*b12 + a12*b22],
            [a21*b11 + a22*b21, a21*b12 + a22*b22]
        ]

        return render_template('result.html', result=result)

    except ValueError:
        return "Please enter valid integers only."

if __name__ == '__main__':
    app.run(debug=True)
