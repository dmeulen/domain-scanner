import os


class Config(object):
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
    ES_URL = os.environ.get('ES_URL', 'http://localhost:9200')
    ES_SNIFF = os.environ.get('ES_SNIFF', False)
    ES_TIMEOUT = os.environ.get('ES_TIMEOUT', 240)
    DNS_ALERT_INDEX = os.environ.get('DNS_ALERT_INDEX', 'dnsalert')
