from myapp import myapp_obj
from myapp.forms import TopCities
from flask import render_template, flash, redirect

from myapp import db
from myapp.models import City

@myapp_obj.route("/", methods=['GET', 'POST'])
def home():
    title = 'Top Cities'
    name = 'Dat Tri'
    form = TopCities()
    list_city=City.query.order_by(City.city_rank).all()

    if form.validate_on_submit():
        cityname = form.city_name.data
        cityrank = form.city_rank.data
        visited = form.is_visited.data
        
        found_city = City.query.filter_by(city_name=form.city_name.data).first()
        if found_city: 
            flash('The City is already exist')
            return redirect('/')
       
        c = City(city_name = cityname, city_rank = cityrank, is_visited = visited)
        db.session.add(c)
        db.session.commit()
        flash('The City is added')
        return redirect('/')


    return render_template("home.html", title=title, name=name, form=form, top_cities=list_city)