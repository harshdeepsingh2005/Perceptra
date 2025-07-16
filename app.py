from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/simulate', methods=['GET', 'POST'])
def simulate():
    prediction = None
    if request.method == 'POST':
        scenario = request.form.get('scenario')
        # Placeholder simulation logic
        if scenario == "pricing":
            prediction = "📈 82% Satisfaction (Optimistic)"
        elif scenario == "delay":
            prediction = "⚠️ 49% Satisfaction (Moderate Risk)"
        elif scenario == "ui":
            prediction = "🧪 65% Satisfaction (Neutral)"
        else:
            prediction = "Unknown Scenario"
        return render_template("results.html", prediction=prediction)
    return render_template('simulate.html')

if __name__ == '__main__':
    app.run(debug=True)
