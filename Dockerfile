FROM alpine:3.9

MAINTAINER Danny van der Meulen <danny@catdevbrain.nl>

ENV \
  ALPINE_MIRROR="nl.alpinelinux.org" \
  ALPINE_VERSION="v3.9" \
  APK_ADD_TEMP="" \
  APK_ADD_PERM="python3 ca-certificates"

EXPOSE 9666

WORKDIR /

COPY app/ /tmp/app

RUN \
  echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/main" > /etc/apk/repositories && \
  echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/community" >> /etc/apk/repositories && \
  apk --no-cache update && \
  apk --no-cache upgrade && \
  apk --no-cache add ${APK_ADD_TEMP} ${APK_ADD_PERM} && \
  cd /tmp/app && \
  python3 setup.py install && \
  apk --purge del ${APK_ADD_TEMP} && \
  rm -rf \
    /tmp/* \
    /var/cache/apk/*

CMD ["gunicorn", "-w4", "--max-requests", "100", "-b", "0.0.0.0:9666", "dnsalert:dnsalert"]
