import smtplib
from flask import Flask, render_template as RenderTemplate, request, redirect, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ICLOUD_USERNAME = "aidangollan@icloud.com"
ICLOUD_APP_PASSWORD = "tohz-nosx-ajwm-yfso"

@app.route('/health')
def health_check():
    return "Healthy", 200

@app.route('/', methods = ["GET", "POST"])
def home():
    return RenderTemplate("index.html")

@app.route('/projects', methods = ["GET", "POST"])
def projects():
    return RenderTemplate("projects.html")

@app.route('/experience', methods = ["GET", "POST"])
def experience():
    return RenderTemplate("experiences.html")

@app.route('/contact', methods = ["POST"])
def contact():
    '''
    when called, send email with message to gollanai@msu.edu from iCloud account
    '''
    user_name = request.form.get('name')
    user_email = request.form.get('email')
    user_message = request.form.get('message')
    
    # Format the email
    subject = "Contact Form Message from {} ({})".format(user_name, user_email)
    body = "{} wrote:\n\n{}".format(user_name, user_message)
    message = "Subject: {}\n\n{}".format(subject, body)

    try:
        # Sending the email using iCloud's SMTP server
        with smtplib.SMTP('smtp.mail.me.com', 587) as server:
            server.starttls()
            server.login(ICLOUD_USERNAME, ICLOUD_APP_PASSWORD)
            server.sendmail(ICLOUD_USERNAME, "gollanai@msu.edu", message)
        
        return jsonify({"message": "Email sent successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
