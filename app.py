from flask import Flask, render_template, request, session
import pickle
import re

app = Flask(__name__)
app.secret_key = "secret123"   # required for session

vector = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("model (1).pkl", 'rb'))

@app.route("/", methods=['GET', 'POST'])
def index():
    
    # initialize history
    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        url = request.form['url']
        
        cleaned_url = re.sub(r'^https?://(www\.)?', '', url)
        
        prediction = model.predict(vector.transform([cleaned_url]))[0]

        if prediction == 'bad':
            result = "Phishing ⚠️"
        elif prediction == 'good':
            result = "Safe ✅"
        else:
            result = "Error"

        # store history (limit to 10)
        history = session["history"]
        history.append({"url": url, "result": result})
        session["history"] = history[-10:]

        return render_template("index.html", predict=result, history=session["history"])

    return render_template("index.html", history=session["history"])


if __name__ == "__main__":
    app.run(debug=True)