import re
import json
from urllib import request

def get_localizacao_atual_by_ip():
    url = 'http://ipinfo.io/json'
    response = request.urlopen(url)
    data = json.load(response)