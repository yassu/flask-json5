from flask import Flask, request, render_template
import json
import json5

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    json5_input = request.form.get('json5_input', '')

    json5_obj = None
    json_output = ""
    error_message = ""
    try:
        json5_obj = get_parsed_json5_obj(json5_input)
    except ValueError as e:
        error_message = format(e)
    if json5_obj is not None:
        json_output = get_output_json_str(json5_obj)

    return render_template(
        'json5_conv.html',
        title='Json5 Converter',
        json5_input=json5_input,
        json_output=json_output,
        error_message=error_message)

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
