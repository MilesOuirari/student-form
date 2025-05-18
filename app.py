from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'secret123'

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    print("Form submitted:", form_data)  # You can save it to DB or Sheets later
    flash("Your application has been submitted successfully.")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
