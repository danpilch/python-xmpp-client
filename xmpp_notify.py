import argparse
import xmpp
import logging

log = logging.getLogger()
log.setLevel('INFO')

class xmpp_notify(object):
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
        jid = xmpp.JID('{0}@{1}'.format(self.args.user, self.args.host))
        user = self.args.user
        host = self.args.host
        port = self.args.port
        password = self.args.password
        message = self.args.message
        
        msg = xmpp.protocol.Message(body=message)
       
        try:
            conn = xmpp.Client(jid.getDomain(), debug=self.args.debug)
            conn.connect(server=(host, port))
            conn.auth(user, password, 'xmpp_notify')
            conn.sendInitPresence(requestRoster=0)
        except Exception as e:
            log.error('Error connecting to XMPP server: {0}'.format(e))
            raise

        log.info('Connected to XMPP server: {0}'.format(host))

        try:
            if self.args.group:
                msg.setType('groupchat')
                msg.setTag('x', namespace='http://jabber.org/protocol/muc#user')
                conn.send(xmpp.Presence(to=self.args.to[0]))
            else:
                msg.setType('chat')
        except Exception as e:
            log.error('Error setting message type: {0}'.format(e))
            raise

        for recipient in self.args.to:
            try:
                msg.setTo('{0}@{1}'.format(recipient, host))
                conn.send(msg)
                log.info('Sent message to user: {0}'.format(recipient))
            except Exception as e:
                log.error('Error sending message to user: {0} {1}'.format(recipient, e))
                continue
        
        conn.disconnect()
        log.info('Disconnected from XMPP server.')

def main():
    logging.basicConfig()

    mail = xmpp_notify()
    mail.send_message()

if __name__ == "__main__":
    main()
