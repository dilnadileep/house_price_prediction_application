from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///houses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# House model
class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    income = db.Column(db.Float, nullable=False)
    age = db.Column(db.Float, nullable=False)
    rooms = db.Column(db.Float, nullable=False)
    bedrooms = db.Column(db.Float, nullable=False)
    population = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(500), nullable=False)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Form submission route
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        income = request.form['income']
        age = request.form['age']
        rooms = request.form['rooms']
        bedrooms = request.form['bedrooms']
        population = request.form['population']
        price = request.form['price']
        address = request.form['address']

        # Create a new House object
        new_house = House(
            income=income,
            age=age,
            rooms=rooms,
            bedrooms=bedrooms,
            population=population,
            price=price,
            address=address
        )

        # Add to the database
        try:
            db.session.add(new_house)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            return f"There was an issue adding the house: {e}"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database and tables
    app.run(debug=True)
