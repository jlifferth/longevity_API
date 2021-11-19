from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World! It may not look like much now, but this is the beginning of\n' \
           'the longevity API!'

