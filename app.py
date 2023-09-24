import smtplib
from flask import Flask, render_template as RenderTemplate, request, redirect, jsonify
from flask_cors import CORS
import os
#from dotenv import load_dotenv
#load_dotenv()

app = Flask(__name__)
CORS(app)

ICLOUD_USERNAME = os.getenv("ICLOUD_USERNAME")
ICLOUD_APP_PASSWORD = os.getenv("ICLOUD_APP_PASSWORD")

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
    print("Received request to send email")  # Debugging statement
    user_name = request.form.get('name')
    user_email = request.form.get('email')
    user_message = request.form.get('message')
    
    # Format the email
    subject = "Contact Form Message from {} ({})".format(user_name, user_email)
    body = "{} wrote:\n\n{}".format(user_name, user_message)
    try:
        # Format the email with explicit From and To headers
        msg = ('From: {}\r\nTo: {}\r\nSubject: {}\r\n\r\n{}'.format(
            ICLOUD_USERNAME,
            "aidangollan@icloud.com",
            subject,
            body
        ))

        print('Sending email to gollanai@msu.edu...')  # Debugging statement
        with smtplib.SMTP('smtp.mail.me.com', 587) as server:
            server.starttls()
            server.login(ICLOUD_USERNAME, ICLOUD_APP_PASSWORD)
            send_status = server.sendmail(from_addr=ICLOUD_USERNAME,
                                        to_addrs="aidangollan@icloud.com",
                                        msg=msg)

        if send_status != {}:
            return jsonify({"error": "There was a problem sending the email."}), 500

        return jsonify({"message": "Email sent successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return the error message

if __name__ == "__main__":
    app.run(debug=True)
