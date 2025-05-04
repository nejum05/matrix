from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Matrix Multiplication</h2>
        <form action="/multiply" method="get">
            <label>Matrix A (rows separated by newlines, elements by spaces):</label><br>
            <textarea name="matrix_a" rows="5" cols="30" placeholder="1 2\n3 4"></textarea><br><br>
            <label>Matrix B (rows separated by newlines, elements by spaces):</label><br>
            <textarea name="matrix_b" rows="5" cols="30" placeholder="5 6\n7 8"></textarea><br><br>
            <input type="submit" value="Multiply">
        </form>
    '''

@app.route('/multiply')
def multiply():
    try:
        matrix_a = request.args.get('matrix_a', '')
        matrix_b = request.args.get('matrix_b', '')

        # Parse input into 2D lists
        a = [list(map(int, row.strip().split())) for row in matrix_a.strip().split('\n')]
        b = [list(map(int, row.strip().split())) for row in matrix_b.strip().split('\n')]

        # Validate matrix multiplication condition
        if len(a[0]) != len(b):
            return "Error: Matrix A columns must equal Matrix B rows."

        # Matrix multiplication logic
        result = [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

        result_str = '<br>'.join([' '.join(map(str, row)) for row in result])
        return f"<h3>Result:</h3><p>{result_str}</p><br><a href='/'>Try Again</a>"

    except Exception as e:
        return f"Error: {str(e)}<br><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
