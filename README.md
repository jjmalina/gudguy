# GudGuy

My IRC bot built with [irctk](https://github.com/maxcountryman/irctk) that sits in #tech@nyu on irc.freenode.net and searches the internets for the gud stuff.
Currently searches [Giphy](http://giphy.com), [SoundCloud](http://soundcloud.com), and [YouTube](http://youtube.com).

* How to add a bot command:

        from gudguy import bot

        @bot.command('mc')  # shortcut
        @bot.command
        def my_command(context):
            command = context.args  # the command that was issued
            return 'Hi.'

* Then in `gudguy/__init__.py` make sure the module your command was defined in is imported.
* All commands must be prefixed with `.`, i.e. `.youtube`

Commands:
* `.g`, `.giphy` searches [Giphy](http://giphy.com). You can add `random` to your query to pull a random gif.
* `.sc`, `.soundcloud_track` searches [SoundCloud](http://soundcloud.com) for tracks.
* `.yt`, `.youtube` searches [YouTube](http://youtube.com).
