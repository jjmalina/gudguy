import requests

from gudguy import bot

base_url = 'http://gdata.youtube.com/feeds/api/'
search_api_url = base_url + 'videos?v=2&alt=jsonc&max-results=1'
video_url = "http://youtube.com/watch?v={0}"


@bot.command('yt')
@bot.command
def youtube(context):
    res = requests.get(search_api_url, params={'q': context.args})
    if not res.status_code == 200:
        return 'Error making request'

    data = res.json()
    if 'error' in data:
        return 'Error performing search.'
    if data['data']['totalItems'] == 0:
        return 'No results.'

    video = data['data']['items'][0]
    return "%s %s" % (video['title'], video_url.format(video['id']))