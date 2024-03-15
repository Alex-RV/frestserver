from flask import Flask, render_template, make_response, send_file
from flask_ngrok import run_with_ngrok
# pip install flask-ngrok
# To run:
# flask run --port=5002
# ngrok http 5002
# Install ngrok with homwbrew first and config auth token
# brew install ngrok/ngrok/ngrok
# ngrok config add-authtoken 

app = Flask(__name__)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
app.config['PROPAGATE_EXCEPTIONS'] = False
app.config['DEBUG'] = True

# run_with_ngrok(app)

@app.route('/')
def index():
    response_text = "Everything works"
    status_code = 200  
    response = make_response(response_text, status_code)
    return response


@app.route('/send-command')
def send_command():
    message_sent = False
    
    if message_sent:
        response_text = "Message sent successfully"
        status_code = 200  
    else:
        response_text = "Message not sent"
        status_code = 501  

    response = make_response(response_text, status_code)
    return response 

if __name__ == '__main__':
    app.run()
