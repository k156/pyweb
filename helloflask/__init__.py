from flask import Flask, g, Response, make_response

app = Flask(__name__)
app.debug = True  


@app.route('/res1')
def res1():
    custom_res = Response("Custom Response", 200, {'test': 'ttt'})
    return make_response(custom_res)

# @app.before_request
# def before_request():
#     print("before_request!!!")
#     g.str = "한글"

# @app.route("/gg")
# def helloworld2():
#     return "Hello World!" + getattr(g, 'str', '111')


@app.route("/")
def helloworld():
    return "Hello Flask World!!!!!!!!!!!!!!11"

 