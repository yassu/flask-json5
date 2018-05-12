from flask import Flask, request, render_template
import json
import json5

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    json5_input = request.form.get('json5_input', '')
    json_output = get_output_json_str(get_parsed_json5_obj(json5_input))
    return render_template(
        'json5_conv.html',
        title='flask test',
        json5_input=json5_input,
        json_output=json_output)

def get_parsed_json5_obj(jstr):
    if jstr == "":
        return ""
    return json5.loads(jstr)

def get_output_json_str(obj):
    if obj == "":
        return ""
    return json.dumps(obj, indent=4)

if __name__ == "__main__":
    app.run(debug=True)
