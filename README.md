# python-xmpp-client
Radically simple Python command line tool for interacting with XMPP servers to send notification messages.

## Requirements

Python 2.6+
Python xmpppy library -> http://xmpppy.sourceforge.net/

## Example Usage

```
python xmpp_cli.py --help

usage: xmpp_cli.py [-h] [-d HOST] [-u USER] [-pw PASSWORD]
                      [-t [TO [TO ...]]] [-g GROUP] [-p PORT] [-m MESSAGE]
                      [-de]

A simple XMPP message sending application

optional arguments:
  -h, --help            show this help message and exit
  -d HOST, --host HOST  The XMPP hostname
  -u USER, --user USER  The username to connect to the host and send message
                        via
  -pw PASSWORD, --password PASSWORD
                        The password associated with the username
  -t [TO [TO ...]], --to [TO [TO ...]]
                        The recipient/s of the message (space separated a b c)
  -g GROUP, --group GROUP
                        The name of the group that should receive the message
  -p PORT, --port PORT  The port to connect via default: 5222
  -m MESSAGE, --message MESSAGE
                        The message to send
  -de, --debug          Enable debug mode


```

## License

MIT / BSD

## Author Information

Created by [Dan Pilch](https://github.com/danpilch) [@danpilch](https://twitter.com/danpilch)

