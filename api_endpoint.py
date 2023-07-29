import pandas as pd
from flask import Flask, request, send_file
from wisc_rapport_builder import Builder

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def run_python_function():
    # Get the dict from the request
    dict = request.json['dict']
    
    # Call the Python function with the integers
    df = pd.DataFrame.from_dict(dict)
    rapport_builder = Builder(df)
    result = rapport_builder.build_rapport()
    
    # Return the result as a docx file
    return send_file(result, as_attachment=True, attachment_filename='wisc_rapport.docx')