from dnsalert import dnsalert
from dnsalert.domain_scanner import scan_domain
from flask import current_app, request, Response

@dnsalert.route('/scandomain')
def scandomain():
    domain = request.args.get('domain', None)
    return Response(scan_domain(domain), mimetype='text/plain')


@dnsalert.route('/health')
def health():
    return Response('OK')