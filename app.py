from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
API_KEY = os.getenv("WEATHER_API_KEY")
print("Loaded API KEY:", API_KEY)

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        print("===================================")
        print("REQUEST URL:", url)

        resp = requests.get(url)

        print("STATUS CODE:", resp.status_code)
        print("RESPONSE BODY:", resp.text)
        print("===================================")

        if resp.status_code == 200:
            weather_data = resp.json()
        else:
            weather_data = {"error": resp.text}

    return render_template("index.html", data=weather_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
