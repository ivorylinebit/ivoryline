from flask import Flask, render_template, abort
import os

app = Flask(__name__)

PRODUCTS = [
    {
        "slug": "dessuadora-ivory",
        "name": "Dessuadora IVORY",
        "price": 49,
        "tag": "Unisex",
        "out_of_stock": True,
        "materials": "Cotó 100%",
        "fit": "Regular fit",
        "care": "Rentat suau a 30ºC",
        "images": ['img/ivory-hoodie-1.jpg', 'img/ivory-hoodie-2.jpg', 'img/ivory-hoodie-3.jpg', 'img/ivory-hoodie-4.jpg', 'img/ivory-hoodie-5.jpg', 'img/ivory-hoodie-6.jpg']
    },
    {
        "slug": "dessuadora-line-001",
        "name": "Dessuadora LINE 001",
        "price": 59,
        "tag": "Limited",
        "out_of_stock": True,
        "materials": "Cotó 80% / Polièster 20%",
        "fit": "Slim fit",
        "care": "Rentat suau a 30ºC",
        "images": ['img/line001-hoodie-1.jpg', 'img/line001-hoodie-2.jpg', 'img/line001-hoodie-3.jpg', 'img/line001-hoodie-4.jpg', 'img/line001-hoodie-5.jpg', 'img/line001-hoodie-6.jpg']
    }
]

def get_product(slug):
    for p in PRODUCTS:
        if p["slug"] == slug:
            return p
    return None

def pick_cover(prod):
    if "variants" in prod and prod["variants"]:
        v0 = prod["variants"][0]
        imgs = v0.get("images", [])
        if imgs:
            return imgs[0]
    if "images" in prod and prod["images"]:
        return prod["images"][0]
    return "img/hero.jpg"

@app.route("/")
def home():
    cards = []
    for p in PRODUCTS:
        cards.append({
            "slug": p["slug"],
            "name": p["name"],
            "price": p["price"],
            "tag": p["tag"],
            "out_of_stock": p["out_of_stock"],
            "img": pick_cover(p)
        })
    return render_template("index.html", products=cards)

@app.route("/collection")
def collection():
    cards = []
    for p in PRODUCTS:
        cards.append({
            "slug": p["slug"],
            "name": p["name"],
            "price": p["price"],
            "tag": p["tag"],
            "out_of_stock": p["out_of_stock"],
            "img": pick_cover(p)
        })
    return render_template("collection.html", products=cards)

@app.route("/product/<slug>")
def product(slug):
    p = get_product(slug)
    if not p:
        return render_template("404.html"), 404
    return render_template("product.html", p=p)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
