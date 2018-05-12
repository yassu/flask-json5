from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hoge"
    return render_template('json5_conv.html', title='flask test', name=name)

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
