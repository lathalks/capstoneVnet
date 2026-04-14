from flask import Flask
app = Flask(__name__)

print("Starting Flask app...") 
@app.route("/")
def home():
    return "Hello from Flask on an Azure Ubuntu VM!"

if __name__ == "__main__":
    # Host '0.0.0.0' allows external connections
    app.run(host='0.0.0.0', port=5000)
