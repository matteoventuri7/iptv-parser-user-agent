from flask import Flask
from urllib.request import urlopen

app = Flask(__name__)

PLAYLIST_URL = 'http://iptv.host/get.php?username=xxxxxxxx&password=xxxxxxxxxx&type=m3u&output=ts'
USER_AGENT = 'User-Agent=VLC'
START_LINE = 'http'

@app.route('/')
def parse_playlist():
    l_result = []
    
    with urlopen(PLAYLIST_URL) as response:
        for l in response:
            l = l.decode('utf-8').rstrip()
            if len(l) > 0:
                if START_LINE in l:
                    l_result.append(l + '|' + USER_AGENT + '\n')
                else:
                    l_result.append(l + '\n')

    s_result = "".join(l_result)

    with open('playlist.m3u','w') as f_playlist:
        f_playlist.write(s_result)
    
    return s_result

app.run(port=65432)

# print(parse_playlist())
