FROM alpine:3.13.1

RUN apt add --no-cache pdns pdns-backend-remote
COPY pdns.conf /etc/powerdns/pdns.conf

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 53

CMD ["pdns_server", "--daemon=no"]