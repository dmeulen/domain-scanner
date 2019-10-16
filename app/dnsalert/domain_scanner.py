from flask import current_app
from checkdmarc import check_domains
import dns.resolver
import dns.query
import datetime
import json


def get_record(domain,record_type):
    results = list()
    try:
        myResolver = dns.resolver.Resolver()
        records = myResolver.query(domain, record_type)
        if record_type == "TXT":
            for result in records:
                results = [item.decode() for item in result.strings]
        else:
            results = [result.address for result in records]
    except(dns.resolver.NoAnswer, dns.exception.Timeout) as e:
        current_app.logger.error(e)
        results = None

    return results


def scan_domain(domain):
    scan_results = {
        'A': get_record(domain, 'A'),
        'AAAA': get_record(domain, 'AAAA'),
        'TXT': get_record(domain, 'TXT'),
        'DMARC': check_domains([domain])
    }

    domain_data = {
        'domain': domain,
        'scan_results': scan_results
    }

    # following print statement should be replaced by push to elastic
    print(json.dumps(domain_data))
    current_app.logger.debug(domain_data)

    return 'OK'
