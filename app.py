from flask import Flask, request, jsonify
from models import db, Expense, Budget

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    expense = Expense(**data)
    db.session.add(expense)
    db.session.commit()
    return jsonify({'message': 'Expense added successfully'}), 201

@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([expense.to_dict() for expense in expenses]), 200

if __name__ == "__main__":
    app.run(debug=True)
