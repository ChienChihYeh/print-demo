from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/api/print_pdf', methods=['POST'])
def print_pdf():
    name = request.form['name']
    return render_template('print_pdf.html', name=name) 
    # return name

if __name__ == '__main__':
    app.run(debug=True)