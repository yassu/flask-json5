from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    json5_text = request.form.get('single', '')
    return render_template('json5_conv.html', title='flask test')

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
