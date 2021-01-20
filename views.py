from functools import wraps

from flask import request, abort

from app import app
from controllers import GetApiRates, GetHome, ViewAllRates, UpdateRates, ViewLogs, EditRate, GetContacts
from config import IP_LIST_VAlID

def check_ip(func):
    @wraps(func)
    def checker(*args, **kwds):
        if request.remote_addr not in IP_LIST_VAlID:
            return abort(403)

        return func(*args, **kwds)

    return checker



@app.route('/')
def home_page():
    return GetHome().call()


@app.route('/xrates')
def view_rates():
    return ViewAllRates().call()


@app.route('/api/xrates/<fmt>')
def api_rates(fmt):
    return GetApiRates().call(fmt)


@app.route('/update/<int:from_currency>/<int:to_currency>')
@app.route('/update/all')
def update_xrates(from_currency=None, to_currency=None):
    return UpdateRates().call(from_currency, to_currency)


@app.route('/logs')
@app.route('/logs/<int:pages>')
@check_ip
def view_logs(pages=None):
    return ViewLogs().call(pages)


@app.route('/contacts')
def contacts():
    return GetContacts().call()



@app.route('/edit/<int:from_currency>/<int:to_currency>', methods=['GET', 'POST'])
@check_ip
def edit_xrate(from_currency, to_currency):
    return EditRate().call(from_currency, to_currency)
