from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

recipes = [
    {"id": 1, "title": "Pasta", "ingredients": "Pasta, Tomato, Cheese", "instructions": "Boil pasta. Add sauce. Mix cheese."},
    {"id": 2, "title": "Tea", "ingredients": "Water, Tea leaves, Sugar, Milk", "instructions": "Boil water. Add tea leaves. Add sugar and milk."}
]

@app.route('/')
def index():
    return render_template("index.html", recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    recipe = next((r for r in recipes if r["id"] == recipe_id), None)
    return render_template("recipe.html", recipe=recipe)

@app.route('/add', methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        new_id = len(recipes) + 1
        new_recipe = {
            "id": new_id,
            "title": request.form["title"],
            "ingredients": request.form["ingredients"],
            "instructions": request.form["instructions"]
        }
        recipes.append(new_recipe)
        return redirect(url_for("index"))
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)
