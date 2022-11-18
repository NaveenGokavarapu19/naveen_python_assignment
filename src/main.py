from flask import Flask, request
import os
from models import session,User,Address,inspect




app = Flask(__name__)










@app.route("/add_user")
def add_task():
    user=User(name="ed2",email="212322@",password="aasdsa",profile="121",picture_url= "url",mobile=102013122)
    address = Address(flat_number="104",address1="sea shell121",address2="siripuram12",city="vizag212",state="AP12",pin_code=442341223,user_mail=user.email)
    session.add(user)
    session.commit()
    session.add(address)
    session.commit()
    return "added_data_successfully",200
    



@app.route("/get_registred_users")
def update_task():
    json_body = []
    inst = inspect(User)
    column_names = [c_attr.key for c_attr in inst.mapper.column_attrs]
    results = session.query(User).all()
    for result in results:
        data_list = str(result).split(" ")
        dictionary = dict(zip(column_names,data_list))
        json_body.append(dictionary)

    response = {"result":json_body}
    return response,200

    
    



if __name__=="__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Startup script for launching the application ")
    parser.add_argument("-p","--port",help="port which is used to run flask",type=int,default=5000)
    args = parser.parse_args()
    os.environ['FLASK_PORT'] = str(args.port)
    flask_port = int(os.environ.get('FLASK_PORT'))
    app.run(host="0.0.0.0",port=f'{flask_port}',debug=True)
