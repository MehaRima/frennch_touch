from flask import Flask, request, render_template, redirect, url_for
import os
import json
import random
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', mapsApiKey = os.environ.get('MAPSAPIKEY'))

@app.route('/search', methods=['POST'])
def search():
    content = json.dumps({'la':'la'})
    return redirect(url_for('results', content=content))
    

@app.route('/results')
def results():
    #content = request.args['content']
    #print(content)
    drivers = ['Bonaventure', 'Thomas', 'Adeoke', 'Elysée', 'Ange', 'Kodjovi', 'Mohamed', 'Moutala', 'Ibrahim']
    number_of_results = random.randint(1,4)
    buses = []
    for i in range(number_of_results):
        time_to_departure = random.randint(1,7)
        driver = random.choice(drivers)
        drivers.remove(driver)
        buses.append({
                'id': i,
                'driver': {'name': driver , 'rating': random.randrange(25, 50, 1)/10},
                'time_to_arrival': random.randint(time_to_departure, 30),
                'time_to_departure': time_to_departure,
                'number_of_seats': random.randrange(1, 12),
                'price': random.randrange(200,300)
            })
    return render_template('results.html', buses=buses)


