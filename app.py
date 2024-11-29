from flask import Flask, request, render_template
from scipy.stats import norm

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def laplace_table():
    result = None
    if request.method == 'POST':
        try:
            x = float(request.form['x_value'])
            # Handle Φ(-x) = 1 - Φ(x)
            phi = norm.cdf(x) if x >= 0 else 1 - norm.cdf(-x)
            result = f"Φ({x}) = {phi:.5f}"
        except ValueError:
            result = "Invalid input. Please double check your input."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
