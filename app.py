from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
app = Flask(__name__)
app.secret_key = 'secret123'

# Email configuration (Gmail example)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'eunistud@gmail.com'
app.config['MAIL_PASSWORD'] = 'kwcp idub nnef zewd'
app.config['MAIL_DEFAULT_SENDER'] = 'eunistud@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    form = request.form.to_dict()


    msg_body = f"""
    New Student Application Submitted

    Name: {form.get('name')}
    Email: {form.get('email')}
    Phone: {form.get('phone_code', '') + form.get('phone_number', '')}
    Date of Birth: {form.get('dob')}
    Nationality: {form.get('nationality')}
    Education Level: {form.get('education')}
    Field of Study: {form.get('field')}
    GPA: {form.get('gpa')}
    Languages: {form.get('languages')}

    Preferred Specialties:
    1. {form.get('speciality_1')}
    2. {form.get('speciality_2')}
    3. {form.get('speciality_3')}

    Preferred Countries:
    1. {form.get('Country 1')}
    2. {form.get('Country 2')}
    3. {form.get('Country 3')}

    Program Level: {form.get('program')}
    Start Date: {form.get('start_date')}

    Notes:
    {form.get('notes')}
    """

    msg = Message("New Study Abroad Application", recipients=["alhafezhussien@yahoo.com"], body=msg_body)
    mail.send(msg)

    flash("Application submitted successfully! We'll contact you soon.")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
