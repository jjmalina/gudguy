from gudguy import bot

import soundcloud

client = soundcloud.Client(client_id=bot.config['SOUNDCLOUD_CLIENT_ID'])


@bot.command('sc')
@bot.command
def soundcloud_track(context):
    query = context.args
    tracks = client.get('/tracks', q=query)
    if not tracks:
        return 'Welp.'
    track = tracks[0]
    return "%s %s" % (track.obj['title'], track.obj['permalink_url'])
