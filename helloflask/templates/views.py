from flask import render_template, request, Response
from datetime import datetime, date
from helloflask import app
from helloflask.classes import FormInput
from sqlalchemy.exc import SQLAlchemyError

@app.route('/')
def idx():
    try:
        u = User('abc@efg.com', 'hong')
        db_session.add(u)

    except SQLAlchemyError AS sqlerr:
        db_session.rollback()
        print('SQLErr', sqlerr)

    except:
        print('Error!!')

    return 'RET=' +str(ret)