from flask import Flask, render_template

app = Flask(__name__)

COLORS = ["#FFE600", "#EF57A0", "#3DB6FB", "#A1E689", "#E67979", "#FFB185", "#89EAEA", "#B0B8FF", "#00bbff"]
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/post-wall")
def wall():
    return render_template("wall.html", colors=COLORS)

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/contact-details")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()