from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


app = Flask(__name__)
app.secret_key = "granthbagadiagranthbagadia"


class CarForm(FlaskForm):
    car = StringField('Car Number eg. 0001', validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField('Submit')


class ParkForm(FlaskForm):
    park = StringField('Parking Number eg. 0001', validators=[DataRequired(), Length(min=3, max=7)])
    submit = SubmitField('Submit')


f = open("CC.txt")
a = [i.split(",") for i in f.readlines()]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/car", methods=['GET', 'POST'])
def car():
    form = CarForm()
    car_data = form.car.data
    posts = []
    if form.validate_on_submit():
        for i in a:
            car_data = car_data.upper()
            if car_data in i[4]:
                p = []
                p.append(f"Flat Number: {i[0]}")
                p.append(f"Car Number: {i[4]}")
                p.append(f"Intercom: {i[1]}")
                posts.append(p)
            if car_data in i[5]:
                p = []
                p.append(f"Flat Number: {i[0]}")
                p.append(f"Car Number: {i[5]}")
                p.append(f"Intercom: {i[1]}")
                posts.append(p)
        if posts == []:
            posts.append(["Car Number Not Available"])
        return render_template('car.html', title = 'Request car Data', form = form, posts = posts)
    else:
        posts = []
        return render_template('car.html', title = 'Request car Data', form = form, posts = posts)


@app.route("/park", methods=['GET', 'POST'])
def park():
    form = ParkForm()
    park_data = form.park.data
    posts = []
    if form.validate_on_submit():
        for i in a:
            if park_data in i[2]:
                p = []
                p.append(f"Flat Number: {i[0]}")
                p.append(f"Parking Number: {i[2]}")
                p.append(f"Intercom: {i[1]}")
                posts.append(p)
            if park_data in i[3]:
                p = []
                p.append(f"Flat Number: {i[0]}")
                p.append(f"Parking Number: {i[3]}")
                p.append(f"Intercom: {i[1]}")
                posts.append(p)
        if posts == []:
            posts.append(["Parking Number Not Available"])
        return render_template('park.html', title = 'Request car Data', form = form, posts = posts)
    else:
        posts = []
        return render_template('park.html', title = 'Request car Data', form = form, posts = posts)


@app.route("/emergency")
def emergency():
    return render_template('emergency.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 500


if __name__ == '__main__':
    app.run(debug=True)