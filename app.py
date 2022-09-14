from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
csrf.init_app(app)


@app.route('/')
def index():
    return 'Hello World!!'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
