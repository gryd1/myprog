from flask import Flask, request, abort, g
import time
import json

app = Flask(__name__)

# граничение количества запросов до 240 запросов в час


def get_identifiers():
    ret = ['ip:' + request.remote_addr]
    if g.user.is_authenticated():
        ret.append('user:%s' % g.user.get_id())
    return ret


def over_limit(conn, duration=3600, limit=240):
    pipe = conn.pipeline(transaction=True)
    bucket = ':%i:%i' % (duration, time.time() // duration)
    for id in get_identifiers():
        key = id + bucket

        pipe.incr(key)
        pipe.expire(key, duration)
        if pipe.execute()[0] > limit:
            return True

    return False


def over_limit_multi(conn, limits=[(1, 10), (60, 120), (3600, 240)]):
    for duration, limit in limits:
        if over_limit(conn, duration, limit):
            return True
    return False


def over_limit_multi_lua(conn, limits=[(1, 10), (60, 125), (3600, 250)]):
    if not hasattr(conn, 'over_limit_multi_lua'):
        conn.over_limit_multi_lua = conn.register_script(over_limit_multi_lua_)

    return conn.over_limit_multi_lua(
        keys=get_identifiers(), args=[json.dumps(limits), time.time()])


over_limit_multi_lua_ = '''
local limits = cjson.decode(ARGV[1])
local now = tonumber(ARGV[2])
for i, limit in ipairs(limits) do
    local duration = limit[1]

    local bucket = ':' .. duration .. ':' .. math.floor(now / duration)
    for j, id in ipairs(KEYS) do
        local key = id .. bucket

        local count = redis.call('INCR', key)
        redis.call('EXPIRE', key, duration)
        if tonumber(count) > limit[2] then
            return 1
        end
    end
end
return 0
'''


@app.route('/add', methods=['GET', 'POST'])
def add():
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
        z = x + y
        return str(z)
    except:
        return abort(422)


@app.route('/minus')
def minus():
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
        z = x - y
        return str(z)
    except:
        return abort(422)


@app.route('/multi')
def multiplication():
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
        z = x * y
        return str(z)
    except:
        return abort(422)


@app.route('/divi')
def division():
    try:
        y = int(request.args.get('y'))
        if y != 0:
            x = int(request.args.get('x'))
            z = x / y
            return str(z)
        else:
            return abort(422)
    except:
        return abort(422)


@app.route('/subs')
def substraction():
    try:
        index = int(request.args.get('index'))
        if index > 0:
            index = index - 1
            lens = int(request.args.get('lens'))
            if lens > 0:
                lens = lens + index
                string = request.args.get('string')
                result = list(string)
                slices = result[index:lens]
                mystring = ''.join(slices)
            else:
                return abort(422)
            return mystring
        else:
            return abort(422)
    except:
        return abort(422)


@app.route('/upp')
def upper():
    try:
        string = request.args.get('string')
        if string != '':
            result = string.upper()
            return result
        else:
            return abort(422)
    except:
        return abort(422)


@app.route('/low')
def lower():
    try:
        string = request.args.get('string')
        if string !='':
            result = string.lower()
            return result
        else:
            return abort(422)
    except:
        return abort(422)


if __name__ == "__main__":
    app.run(debug=True)
