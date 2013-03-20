# -*- coding: utf-8 -*-

"""
Consume the Giphy API -- http://giphy.com/
i.e. 'http://giphy.com/api/gifs?tag=cat'
"""
import random
import requests
import urllib

from gudguy import bot
from gudguy.utils import timestamp_utcnow

GIPHY_API = 'http://giphy.com/api'


def search_api_url(**kwargs):
    endpoint = '/gifs?%s' % (urllib.urlencode(kwargs))
    return GIPHY_API + endpoint


def search_api_request(query):
    res = requests.get(search_api_url(tag=query))
    return res.json() if res.status_code == 200 else None


def search_gifs(query):
    content = search_api_request(query)
    return content['data'] if content is not None else None


def get_gif(gifs, random_gif=False):
    if random_gif:
        return random.choice(gifs)
    return gifs[0]


@bot.command('g')
@bot.command
def giphy(context):
    query = context.args
    opts = {'random_gif': 'random ' in query}
    query = query.replace('random ', '') if opts['random_gif'] else query
    query = query.replace(' ', '-')
    gifs = search_gifs(query)
    if not gifs:
        return 'Welp.'
    return get_gif(gifs, **opts)['image_original_url']
