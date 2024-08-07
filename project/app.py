from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import joblib
model = joblib.load('house_price_model_rf.pkl')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///houses.db'
db = SQLAlchemy(app)

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    income = db.Column(db.Float, nullable=False)
    age = db.Column(db.Float, nullable=False)
    rooms = db.Column(db.Float, nullable=False)
    bedrooms = db.Column(db.Float, nullable=False)
    population = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        try:
            income = float(request.form['income'])
            age = float(request.form['age'])
            rooms = float(request.form['rooms'])
            bedrooms = float(request.form['bedrooms'])
            population = float(request.form['population'])
            address = request.form['address']

            # Predict the house price using the new model
            features = [[income, age, rooms, bedrooms, population]]
            predicted_price = model.predict(features)[0]

            new_house = House(
                income=income,
                age=age,
                rooms=rooms,
                bedrooms=bedrooms,
                population=population,
                address=address
            )

            db.session.add(new_house)
            db.session.commit()

            # Retrieve the latest entry added
            last_house = House.query.order_by(House.id.desc()).first()
            return render_template('house_details.html', house=last_house, predicted_price=predicted_price)
        except ValueError:
            return "Invalid input. Please enter numerical values for the required fields."
        except Exception as e:
            return f"There was an issue adding the house: {e}"

@app.route('/house_details')
def house_details():
    # Retrieve the latest entry added
    last_house = House.query.order_by(House.id.desc()).first()
    return render_template('house_details.html', house=last_house)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
