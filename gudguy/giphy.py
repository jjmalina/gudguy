# -*- coding: utf-8 -*-

"""
Consume the Giphy API -- https://github.com/Giphy/GiphyAPI
i.e. 'http://api.giphy.com/v1/gifs/translate?s=superman&api_key=dc6zaTOxFJmzC'
"""
import random
import requests
import urllib

from gudguy import bot
from gudguy.utils import response_json_or_none

GIPHY_API = 'http://api.giphy.com/v1/gifs'
GIPHY_KEY = 'dc6zaTOxFJmzC'


def giphy_api_url(endpoint, **kwargs):
    kwargs['api_key'] = GIPHY_KEY
    return "%s%s?%s" % (GIPHY_API, endpoint, urllib.urlencode(kwargs))


@response_json_or_none
def search_api_request(query):
    return requests.get(giphy_api_url('/search', q=query))


def search_gifs(query):
    json = search_api_request(query)
    return json['data'] if (json is not None and 'data' in json) else None


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
    return get_gif(gifs, **opts)['images']['original']['url']
