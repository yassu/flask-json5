from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    json5_input = request.form.get('json5_input', '')
    return render_template(
        'json5_conv.html',
        title='flask test',
        json5_input=json5_input)

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
