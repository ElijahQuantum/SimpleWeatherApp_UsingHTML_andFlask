from flask import Flask , request , render_template
from weather_api import get_weather_info    

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("web.html", city=None, weather=None, unit="metric", error=None)

@app.route("/weather", methods=["POST"])
def main():
    city = request.form.get("city", "").strip()
    unit = request.form.get("unit", "metric").strip().lower()

    if not city:
        return render_template("web.html", city=None, weather=None, unit=unit, error="Please enter a city.")

    if unit not in ["metric", "imperial"]:
        return render_template("web.html", city=city, weather=None, unit="metric", error="Invalid unit. Use 'metric' or 'imperial'.")

    weather_info = get_weather_info(city, unit)
    return render_template("web.html", city=city, weather=weather_info, unit=unit, error=None)

if __name__ == "__main__":
    app.run(debug=True)


