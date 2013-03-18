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
* All command must be prefixed with `.`, i.e. `.youtube`
