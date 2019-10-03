#!/usr/bin/python


from flask import Flask

# Setup Flask app.
app = Flask(__name__)
app.debug = True


# Routes
@app.errorhandler(Exception)
def unhandled_exception(e):
    return str(e), 500


@app.route('/')
def root():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, use_reloader=True)
