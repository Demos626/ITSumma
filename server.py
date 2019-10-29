import flask, os, json, redis
from dotenv import load_dotenv
from urllib.parse import urlparse


load_dotenv()
WEB_SERVER_URL = os.getenv('WEB_SERVER_URL')
log = redis.StrictRedis(host='localhost', port=6379)
app = flask.Flask(__name__)



@app.route('/', methods=['GET'])
def get_test():
    temp = {}
    pspar = flask.request.args.get('topics')
    now_par = json.loads(log.execute_command('JSON.GET', 'log', '[-1]'))


    for count, base_key in enumerate(json.loads(log.execute_command('JSON.GET', 'log', '.'))):
        for key in pspar.split(','):
            if key in base_key:
                print(base_key[key][-1])
                temp[key] = float(base_key[key][-1][key])
    return flask.jsonify(temp)

    
if __name__ == '__main__':
    app.run(host = urlparse(WEB_SERVER_URL).hostname, port = int(urlparse(WEB_SERVER_URL).port))
