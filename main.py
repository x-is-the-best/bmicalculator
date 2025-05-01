from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height, units):
    if units == "metric":
        height_m = height / 100  # cm to meters
    else:  # imperial
        weight = weight * 0.453592
        height = height * 0.0254
        height_m = height

    bmi = weight / (height_m ** 2)
    return round(bmi, 1)

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = category = error = None

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            units = request.form.get("units", "metric")
            bmi = calculate_bmi(weight, height, units)
            category = get_category(bmi)
        except ValueError:
            error = "Please enter valid numbers for weight and height."

    return render_template("index.html", bmi=bmi, category=category, error=error)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)

