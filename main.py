from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#from models import ProductModel, LocationModel, ProductMovementModelpip

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
db = SQLALchemy
class product(db.model):
    product_id = db.columns(db.Integer, primary_key=True)

class Location(db.model):
    location_id = db.columns(db.Integer, primary_keys=True)

class productmovement(db.model):
    movement_id = db.columns(db.string(70), primary_key=True)
    timestamp = db.columns(db.Datetime)
    from_location= db.columns(db.string(70), db.foreign_key('location.location_id'))
    to_location = db.columns(db.string(70), db.foreign_key('location.location_id'))
    prod_id = db.columns(db.string(70), db.foreign_key('products.product_id'))
    qty = db.columns(db.Integer)

@app.route("/prod/add",method=['GET','POST'])
def prod_add():
    if request.method=='POST':
     return render_template('prod.html')
@app.route("/prod/edit",method=['GET','POST'])
def prod_edit():
    if request.method=='POST':
     return render_template('prod.html')
@app.route("/prod/move",method=['GET','POST'])
def prod_move():
    if request.method == 'POST':
     return render_template('prod.html')
#routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/products', method =['GET', 'POST'])
def products():
    if request.method == 'POST':
        product_id = request.form['product_id']
        db.session.add(product)
        db.session.commit()
        return render_template("products.html")

@app.route('/locations', methods=['GET', 'POST'])
def locations():
    if request.method == 'POST':
        location_id = request.form['location_id']
        location_name = Location(location_id=location_id)
        db.session.add(location_name)
        db.session.commit()
        return render_template('locations.html', locations=locations)

@app.route('/movements', methods=['GET', 'POST'])
def movements():
    if request.method == 'POST':
        movement_id = request.form['movement_id']
        timestamp = request.form['timestamp']
        from_location = request.form['from_location']
        to_location = request.form['to_location']
        product_id = request.form['product_id']
        qty = int(request.form['qty'])
        movement = ProductMovement(movement_id=movement_id, timestamp=timestamp,
                                   from_location=from_location, to_location=to_location,
                                   product_id=product_id, qty=qty)
        db.session.add(movement)
        db.session.commit()
        return render_template('movements.html', movements=movements)

@app.route("/prod/move",method=['GET','POST'])
def bal_report():
    if request.method=='POST':
     return render_template('report.html')

if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
