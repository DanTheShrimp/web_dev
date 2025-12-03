#DD Period 7 Flask Notes
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        return redirect(url_for("user", name=request.form["name"]))
    return render_template("index.html")

@app.route("/slugwiki")
def contact():
    return "<p> Doomslug is a yellow slug with blue spikes along her backside. She does not appear to have eyes, a mouth, or any of the components of a face, but her behavior reminds Spensa of a chipmunk. When pleased, Doomslug emits a flutelike trill from her spikes. As a taynix, Doomslug has the ability to travel at faster-than-light speeds by accessing the nowhere and can distract the delvers from the cytonic hyperjump so that they won't be drawn into the universe. It is unclear whether or not Doomslug has or could learn any other cytonic powers. She also has the ability to shapeshift and disguise herself as other objects, as seen when she transforms into Spensa's father's flight pin. Doomslug can replicate any sound she hears with impeccable precision, though there is always a 'distinctly fluty' sound to it. She is also capable of slightly modifying the sounds she mimics, as shown when she accidentally corrects Spensa's grammar by saying 'By whom!' in response to the question 'By who?' Doomslug is covered in blue spikes, which would make handling her difficult, and provides protection from predators. Her bright colors also lead Spensa to believe the possibility that she might be poisonous. The Superiority database says that the taynix are dangerously venomous. She is also capable of resisting minor increases in gravitational forces.</p>"

@app.route("/contact")
def contactihateyou():
    return render_template("contact.html")

@app.route("/<name>")
def user(name):
    return f"<h6>Hello {name}!</h6>"

if __name__ == "__main__":
    app.run(debug=True)