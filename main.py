from pexpect import pxssh


class BotNet:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.ssh()

    def ssh(self):
        try:
            bot = pxssh.pxssh()
            bot.login(self.host, self.user, self.password)
            return bot
        except Exception as e:
            print('Connection Failure.')
            print(e)

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


def add_bot(host, user, password):
    new_bot = BotNet(host, user, password)
    bot_net.append(new_bot)


def command_bots(command):
    for bot in bot_net:
        attack = bot.send_command(command)
        print("Output from " + bot.host)
        print(attack)


bot_net = []
add_bot('', '', '')
command_bots('ls')
