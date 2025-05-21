from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        try:
            matrix_a = eval(request.form['matrix_a'])
            matrix_b = eval(request.form['matrix_b'])

            # Validate multiplication rules
            if len(matrix_a[0]) != len(matrix_b):
                error = "Number of columns in Matrix A must equal number of rows in Matrix B"
            else:
                result = []
                for i in range(len(matrix_a)):
                    row = []
                    for j in range(len(matrix_b[0])):
                        cell = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_b)))
                        row.append(cell)
                    result.append(row)
        except Exception as e:
            error = f"Invalid input: {e}"

    return render_template('index.html', result=result, error=error)
