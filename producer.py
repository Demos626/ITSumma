import psutil, sched, time, os, requests, sys, random
from dotenv import load_dotenv


load_dotenv()
RECEIVER_URL = os.getenv('RECEIVER_URL')
INTERVAL = os.getenv('INTERVAL')
print('Press CTRL+C to quit')


try:
    while True:
        ps_stat = {'cpu': psutil.cpu_percent(float(INTERVAL)), 'gpu': float("%.1f" % (random.random()*100))}
        print(ps_stat)
        requests.post(RECEIVER_URL, json = ps_stat)
except KeyboardInterrupt:
    print('Stop service.\nNow param =', {'cpu': psutil.cpu_percent(1), 'gpu': float("%.1f" % (random.random()*100))})
    sys.exit()
