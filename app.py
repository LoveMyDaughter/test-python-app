from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {'message': 'Hello from k8s! Antonio is testing this out...'}

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# ```

# Create `requirements.txt`:
# ```
# Flask==2.3.0