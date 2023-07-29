from flask import Flask, request
import wisc_rapport_builder

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def run_python_function():
    # Get the integers from the request
    integers = request.json['integers']
    
    # Call the Python function with the integers
    result = wisc_rapport_builder.Builder(integers)
    
    # Return the result as a docx file
    return send_file(result, as_attachment=True, attachment_filename='result.docx')