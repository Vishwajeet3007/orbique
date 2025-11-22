from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for storing Q&A pairs
class QA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f"<QA {self.id} - {self.question}>"

# Route to serve the chatbot responses
@app.route('/get-response', methods=['POST'])
def get_response():
    user_input = request.json.get('question')
    if not user_input:
        return jsonify({"error": "No question provided"}), 400

    # Search for the question in the database
    qa = QA.query.filter(QA.question.ilike(f"%{user_input}%")).first()
    
    if qa:
        return jsonify({"answer": qa.answer})
    else:
        return jsonify({"answer": "Sorry, I don't have an answer for that question."})

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')  # Make sure you have 'index.html' in a 'templates' folder

# Ensure the app context is pushed for database operations
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
