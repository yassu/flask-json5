from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    print('form:')
    print(request.form)
    name = "Hoge"
    json5_text = request.form.get('single', '')
    print('json5_text: {}'.format(json5_text))
    return render_template('json5_conv.html', title='flask test', name=name)

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
