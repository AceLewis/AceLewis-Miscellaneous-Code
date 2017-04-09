import time
import shutil

import requests


def get_data():
    url = 'https://www.reddit.com/api/place/board-bitmap'
    response = requests.get(url, stream=True)
    out_filename = 'data/{}_board-bitmap.data'.format(int(time.time()))

    with open(out_filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response


while True:
    try:
        get_data()
        print('{}:sucess'.format(int(time.time())))
    except:
        print('{}:failed'.format(int(time.time())))
        pass
    time.sleep(5 * 60)
