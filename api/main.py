from flask import Flask, request, send_file
from wisc_rapport_builder import Builder
from io import BytesIO

app = Flask(__name__)

@app.route('/api/', methods=['POST'])
def run_python_function():
    # Get the dict from the request
    dict = request.json['listOfDictionaries']
    
    # Call the Python function with the integers
    #df = pd.DataFrame.from_dict(dict)
    #rapport_builder = Builder(dict)
    rapport_builder= Builder(dict)
    save_name = "wisc_rapport.docs"
    result = rapport_builder.build_rapport(save_name)

    
    #Save result to bytes-like object
    output = BytesIO()
    result.save(output)
    output.seek(0)

    print("Retrieved repport, returning file!")

    # Return the result as a docx file
    return send_file(output, as_attachment=True, download_name=save_name)




if __name__ == '__main__':
    #print("Successfully received request!")
    #app.run()
    # if ran below, it will be available to everyone on network (i think)
    app.run(host='0.0.0.0')