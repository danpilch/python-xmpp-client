import argparse
import xmpp
import logging

log = logging.getLogger()
log.setLevel('INFO')

class xmpp_notify(object):

    def send_message(self, host, user, password, to, group, port, message, debug):

        jid = xmpp.JID('{0}@{1}'.format(user, host))
        msg = xmpp.protocol.Message(body=message)
       
        try:
            conn = xmpp.Client(jid.getDomain(), debug=debug)
            conn.connect(server=(host, port))
            conn.auth(user, password, 'xmpp_notify')
            conn.sendInitPresence(requestRoster=0)
        except Exception as e:
            log.error('Error connecting to XMPP server: {0}'.format(e))
            raise

        log.info('Connected to XMPP server: {0}'.format(host))

        try:
            if group:
                msg.setType('groupchat')
                msg.setTag('x', namespace='http://jabber.org/protocol/muc#user')
                conn.send(xmpp.Presence(to=to[0]))
            else:
                msg.setType('chat')
        except Exception as e:
            log.error('Error setting message type: {0}'.format(e))
            raise

        for recipient in to:
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
