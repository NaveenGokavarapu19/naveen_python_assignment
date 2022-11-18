from flask import Flask, request, render_template
import os


app = Flask(__name__)


@app.route("/add")
def add_task():
    data = {'name': 'nabin khadka'}
    return data, 200
    


@app.route("/update")
def update_task():
    pass



if __name__=="__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Startup script for launching the application ")
    parser.add_argument("-p","--port",help="port which is used to run flask",type=int,default=5000)
    args = parser.parse_args()
    os.environ['FLASK_PORT'] = str(args.port)
    flask_port = int(os.environ.get('FLASK_PORT'))
    app.run(host="0.0.0.0",port=f'{flask_port}')
