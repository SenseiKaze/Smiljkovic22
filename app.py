from flask import Flask, render_template, jsonify

app = Flask(__name__)

restorani = {
    "pastica": {
        "naziv": "Pastica",
        "meni": ["Pica", "Pasta", "Lazanje", "Sendvič"]
    },
    "picatim": {
        "naziv": "Pica Tim",
        "meni": ["Margarita", "Capricciosa", "Vesuvio", "Piletina"]
    },
    "hashub": {
        "naziv": "HasHub",
        "meni": ["Burger", "Cheeseburger", "Pomfrit", "Pileći burger"]
    },
    "sahara": {
        "naziv": "Sahara",
        "meni": ["Ćevapi", "Pljeskavica", "Piletina", "Pomfrit"]
    },
    "abc": {
        "naziv": "ABC",
        "meni": ["Sendvič šunka", "Sendvič sir", "Hot Dog", "Kroasan"]
    },
    "lele": {
        "naziv": "Lele",
        "meni": ["Giros", "Pomfrit", "Pileći štapići", "Burger"]
    },
    "oskar": {
        "naziv": "Oskar",
        "meni": ["Palačinke", "Sladoled", "Vafli", "Krofne"]
    },
    "capcap": {
        "naziv": "Cap Cap",
        "meni": ["Espresso", "Cappuccino", "Topla čokolada", "Limunada"]
    },
    "promenada": {
        "naziv": "Promenada",
        "meni": ["Piletina", "Pomfrit", "Burger", "Sendvič"]
    }
}

@app.route("/")
def index():
    restorani= ["Pastica", "Pica Tim", "HasHub", "Sahara", "ABC", "Lele", "Oskar", "Cap Cap", "Promenada"]
    return render_template("index.html", 
                         naslov="Spisak restorana", 
                         spisak=restorani)

@app.route("/restorani")
def svi_restorani():
    return render_template("restorani.html", 
                         naslov="Svi restorani", 
                         spisak=list(restorani.keys()), 
                         restorani=restorani)

@app.route("/restoran/1")
def meni_restorana():   
    meni= ["Margarita", "Capricciosa", "Vesuvio", "Piletina"]    
    return render_template("meni.html", 
                            naslov="Pastica", 
                            meni=meni)
   

@app.route("/primer-niz")
def niz():
    return jsonify([1, 2, 3, 4, 5])

@app.route("/primer-json")
def primer_json():
    return jsonify({"poruka": "Ovo je JSON", "status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)