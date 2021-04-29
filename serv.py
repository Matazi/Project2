from flask import *
import json, csv
from pprint import pprint



app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return app.send_static_file('index.html')

map = {}
with open('datasets/countries-50m.json') as f:
    map = json.load( f )
@app.route('/map')
def worldmap():
    return jsonify( map )


with open('volcanos.json') as f:
    volcanos = json.load( f )
    volcanos = {int(k):v for k,v in volcanos.items()}


@app.route('/volcanos')
def volcano():

    population_within_5_km = request.args.get('pop5km', None, type=float)
    print(population_within_5_km)
    population_within_10_km = request.args.get('pop5km', None, type=float)
    population_within_30_km = request.args.get('pop5km', None, type=float)
    population_within_100_km = request.args.get('pop5km', None, type=float)
    primary_volcano_type = request.args.get('pop5km', None, type=float)

    vfinal = []
    for v in volcanos.values():
            #Filter criteria
            if primary_volcano_type is not None:
                continue
            if population_within_5_km is not None:
                continue
            if population_within_10_km is not None:
                continue
            if population_within_30_km is not None:
                continue
            if population_within_100_km is not None:
                continue

            vfinal.append(v)
    return jsonify(vfinal)


with open('events.json') as f:
    events = json.load( f )
    events = {int(k):v for k,v in events.items()}
@app.route('/events')
def event():


    #Filter criteria


    efinal = []
    for v in events.values():
        efinal.append(v)
    return jsonify(efinal)

with open('eruptions.json') as f:
    eruptions = json.load( f )
    eruptions = {int(k):v for k,v in eruptions.items()}
@app.route('/eruptions')
def eruption():

    erfinal = []
    for v in eruptions.values():
        erfinal.append(v)
    return jsonify(erfinal)







if __name__ == '__main__':
    app.run(host='0.0.0.0',port='9999')
