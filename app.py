from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Production Line Monitor</title>
        </head>

        <body>
            <h1>Production Line Monitor</h1>

            <h2>🟢 LINE STATUS: RUNNING</h2>

            <p>Cars produced: 127</p>
            <p>Current station: Assembly</p>
            <p>Version: 1.1.0</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/status")
def status():
    return {"status": "running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
