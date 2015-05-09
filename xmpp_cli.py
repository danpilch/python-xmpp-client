from xmpp_notify import xmpp_notify
import argparse
import logging

log = logging.getLogger()
log.setLevel('INFO')

class xmpp_cli(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="A simple XMPP message sending application")
        self.parser.add_argument("-d", "--host", help="The XMPP hostname")
        self.parser.add_argument("-u", "--user", help="The username to connect to the host and send message via")
        self.parser.add_argument("-pw", "--password", help="The password associated with the username")
        self.parser.add_argument("-t", "--to", nargs='*', help="The recipient/s of the message (space separated a b c)")
        self.parser.add_argument("-g", "--group", help="The name of the group that should receive the message")
        self.parser.add_argument("-p", "--port", default=5222, help="The port to connect via default: 5222")
        self.parser.add_argument("-m", "--message", help="The message to send")
        self.parser.add_argument("-de", "--debug", action="store_true", help="Enable debug mode")

        self.args = self.parser.parse_args()

    def send_message(self):
        self.mail = xmpp_notify()
        self.mail.send_message(host=self.args.host, user=self.args.user, password=self.args.password, to=self.args.to, \
                                group=self.args.group, port=self.args.port, message=self.args.message, debug=self.args.debug)

def main():
    logging.basicConfig()

    send = xmpp_cli()
    send.send_message()

if __name__ == "__main__":
    main()
