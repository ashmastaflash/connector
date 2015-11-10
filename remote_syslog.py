#!/usr/bin/python

# from http://liftoff.github.com/GateOne/Developer/remote_syslog.html

"""
Python syslog client.

This code is placed in the public domain by the author.
Written by Christian Stigen Larsen.

This is especially neat for Windows users, who (I think) don't
get any syslog module in the default python installation.

See RFC3164 for more info -- http://tools.ietf.org/html/rfc3164

Note that if you intend to send messages to remote servers, their
syslogd must be started with -r to allow to receive UDP from
the network.
"""

import socket

FACILITY = {
    'kern': 0, 'user': 1, 'mail': 2, 'daemon': 3,
    'auth': 4, 'syslog': 5, 'lpr': 6, 'news': 7,
    'uucp': 8, 'cron': 9, 'authpriv': 10, 'ftp': 11,
    'local0': 16, 'local1': 17, 'local2': 18, 'local3': 19,
    'local4': 20, 'local5': 21, 'local6': 22, 'local7': 23,
}

LEVEL = {
    'emerg': 0, 'alert':1, 'crit': 2, 'err': 3,
    'warning': 4, 'notice': 5, 'info': 6, 'debug': 7
}

syslogSocket = None

def openlog():
    global syslogSocket
    syslogSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def syslog(message, level=LEVEL['notice'], facility=FACILITY['daemon'], host='172.31.3.9', port=514):
    """
    Send syslog UDP packet to given host and port.
    """
    try:
        data = '<%d>%s' % (level + facility*8, message)
    except:
        data
        print("level type: ", type(level))
        print(level)
        print("facility type: ", type(facility))
        print(facility)
        print("message type: ", type(message))
        print(message)
    try:
        syslogSocket.sendto(data, (host, port))
    except (AttributeError) as e:
        print("Error message: ", e)
        encode_data = data.encode('utf-8')
        try:
            syslogSocket(encode_data, (host, port))
        except (AttributeError) as e:
            print("Error message after encoding data: ", e)
def closelog():
    syslogSocket.close()
