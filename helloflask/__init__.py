from flask import Flask, g, Response, make_response, request, render_template, Markup
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

app = Flask(__name__)
app.debug = True  


@app.route('/res1')
def res1():
    custom_res = Response("Custom Response", 200, {'test': 'ttt'})
    return make_response(custom_res)

@app.before_request
def before_request():
    print("before_request!!!")
    g.str = "한글"

@app.route("/gg")
def helloworld2():
    return "Hello World!" + getattr(g, 'str', '111')


@app.route("/")
def helloworld():
    return "Hello Flask World!!!!!!!!!!!!!!11"



# def ymd(fmt):
#     def trans(date_str):
#         return datetime.strptime(date_str, fmt)
#     return trans


@app.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    return "우리나라 시간 형식: " + str(datestr)


# @app.route('/home')
# def h():
#     return render_template("main.html")

@app.route('/example')
def ex():
    return render_template("jsh_app.html")




@app.template_filter('simpledate')
def simpledate(dt):
    if not isinstance(dt, date):
        dt = datetime.strptime(dt, '%Y-%m-%d %H:%M')

    # if ( datetime.now() - dt) < timedelta(1):
    if (datetime.now() - dt).days < 1:
        fmt = "%H:%M"
    else:
        fmt = "%m/%d"

    return "<strong>%s</strong>" % dt.strftime(fmt)




@app.route('/2')
def idx():
    today = '2019-02-14 09:22'
    d = datetime.strptime("2019-03-01", "%Y-%m-%d")
    sdt = d.weekday() * -1
    nextMonth = d + relativedelta(months=1)
    mm = d.month
    edt = (nextMonth - timedelta(1)).day + 1
    return render_template('main.html', sdt=sdt, edt=edt, mm=mm, ttt='TestTTT999', radioList=rds, today=today)]


# @app.route('/tmpl2')
# def tmpl2():
#     a = (1, "만남1", "김건모", False, [])
#     b = (2, "만남2", "노사연", True, [a])
#     c = (3, "만남3", "익명", False, [a, b])
#     d = (4, "만남4", "익명", False, [a, b, c])

#     return render_template("index.html", lst2=[a, b, c, d])

# class Nav():
#     def __init__(self, number, title, url = '#', children = []):
#         self.number = number
#         self.title = title
#         self.url = url
#         self.children = children



# @app.route('/tmpl3')
# def tmpl3():
#     jin = Nav(7, 'Jinja', , 'https://www.naver.com/')
#     GC = Nav(8, 'Gensi, Cheetah', 'https://www.naver.com/')
#     py = Nav(4, '파이썬', 'https://www.naver.com/')
#     jv = Nav(5, '자바', 'https://www.naver.com/')
#     flask = Nav(6, '플라스크', 'https://www.naver.com/', [jin, GC])
#     spr = Nav(9, '스프링', 'https://www.naver.com/')
#     njs = Nav(10, '노드js', 'https://www.naver.com/')
#     day = Nav(11, '나의 일상', 'https://www.naver.com/')
#     prg = Nav(1, '프로그래밍 언어', 'https://www.naver.com/', [py, jv])
#     frm = Nav(2, '웹 프레임워크', 'https://www.naver.com/', [flask, spr, njs])
#     etc = Nav(3, '기타', 'https://www.naver.com/', [day])

#     return render_template("index.html", lst=[a, b, c])

@app.route("/tmpl")
def t():
    tit = Markup("<strong>Title</strong>")
    mu = Markup("<h1>iii = <i>%s</i></h1>")
    h = mu % "Italic"
    print("h=", h)

    lst = [("만남1", "김건모", True), ("만남2", "노사연", True),
           ("만남3", "노사봉", False), ("만남4", "아무개", False)]
           
    return render_template('index.html', title=tit, mu=h, lst=lst)