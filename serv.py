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
eruptions = ""
with open('eruptions.json') as f:
    eruptions = json.load( f )
    eruptions = {int(k):v for k,v in eruptions.items()}

@app.route('/volcanos')
def volcano():

    population_within_5_km = request.args.get('pop5km', None, type=float)
    print(population_within_5_km)
    population_within_10_km = request.args.get('pop10km', None, type=float)
    population_within_30_km = request.args.get('pop30km', None, type=float)
    population_within_100_km = request.args.get('pop100km', None, type=float)
    primary_volcano_type = request.args.get('pokm', None, type=float)

    eruption_category = request.args.get('erCat', None)

    time = request.args.get('time', None, type=float)

    vfinal = []
    for v in volcanos.values():
            #Filter criteria
            # if primary_volcano_type is not None:
            #     continue
            # if population_within_5_km is not None:
            #     continue
            # if population_within_10_km is not None:
            #     continue
            if population_within_100_km is not None and float(v['population_within_100_km']) < population_within_100_km:
                continue
            # if population_within_30_km is not None:
            #     continue
            if v['last_eruption_year'] != "Unknown":
                if time is not None and float(v['last_eruption_year']) > time:
                    continue

            vfinal.append(v)
    # erfinal = []
    # for v in eruptions.values():
    #     if eruption_category is not None and v['eruption_category'] == eruption_category:
    #         continue
    #     vfinal.append(v)
    # return jsonify(erfinal)
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

eruptions = ""
with open('eruptions.json') as f:
    eruptions = json.load( f )
    eruptions = {int(k):v for k,v in eruptions.items()}
@app.route('/eruptions')
def eruption():

    eruption_category = request.args.get('erCat', None)

    erfinal = []
    for v in eruptions.values():
        if eruption_category is not None and v['eruption_category'] == eruption_category:
            continue
        erfinal.append(v)
    return jsonify(erfinal)







if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000')
