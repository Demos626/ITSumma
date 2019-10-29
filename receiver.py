import flask, os, json, redis
from dotenv import load_dotenv
from urllib.parse import urlparse


load_dotenv()
RECEIVER_URL = os.getenv('RECEIVER_URL')
app = flask.Flask(__name__)
log = redis.StrictRedis(host='localhost', port=6379)
if log.execute_command('JSON.GET', 'log', '.') == None:
    print('Set Database')
    log.execute_command('JSON.SET', 'log', '.', json.dumps([{'cpu': [{'cpu': 0.0}]}, {'gpu': [{'gpu': 0.0}]}]))

@app.route(urlparse(RECEIVER_URL).path, methods=['POST'])
def home():
    new = flask.request.get_json(force=True)
    for key in new.keys():
        for count, base_key in enumerate(json.loads(log.execute_command('JSON.GET', 'log', '.'))):
            if key in base_key:
                log.execute_command('JSON.ARRAPPEND', 'log', '[{}].{}'.format(count, key), json.dumps({key: new[key]}))
                break
        else:
            log.execute_command('JSON.ARRAPPEND', 'log', '.', json.dumps({key:[{key: new[key]}]}))
    print(new)
    return 'Was added'


@app.route('/clearall')
def clearall():
    for i in reversed(range(len(json.loads(log.execute_command('JSON.GET', 'log'))))):
        log.execute_command('JSON.DEL', 'log', '[{}]'.format(i)) 
    return 'DataBase is clear'


if __name__ == '__main__':
    app.run(host = urlparse(RECEIVER_URL).hostname, port = int(urlparse(RECEIVER_URL).port))
    
 
        