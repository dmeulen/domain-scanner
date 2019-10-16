from flask import Flask
from .config import Config
from elasticsearch import Elasticsearch
import logging

dnsalert = Flask(__name__)
dnsalert.config.from_object(Config)
dnsalert.elasticsearch = Elasticsearch(
    dnsalert.config['ES_URL'].split(','),
    sniff_on_start=dnsalert.config['ES_SNIFF'],
    timeout=dnsalert.config['ES_TIMEOUT']

) if dnsalert.config['ES_URL'] else None

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    dnsalert.logger.handlers = gunicorn_logger.handlers
    dnsalert.logger.setLevel(dnsalert.config['LOG_LEVEL'])

from dnsalert import routes
