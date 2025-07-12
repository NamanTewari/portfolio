from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# Home route serving your HTML
@app.route('/')
def index():
    return render_template('index.html')

# Form submission route
@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "subject": request.form.get("subject"),
        "message": request.form.get("message"),
        "timestamp": datetime.now().isoformat()
    }

    # Save to local JSON file
    os.makedirs("submissions", exist_ok=True)
    with open(f"submissions/{data['name'].replace(' ', '_')}_{datetime.now().timestamp()}.json", "w") as f:
        json.dump(data, f, indent=4)

    return jsonify({"message": "Form submitted successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
