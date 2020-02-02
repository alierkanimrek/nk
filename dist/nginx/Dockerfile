FROM nginx

COPY nginx.conf /etc/nginx
COPY project.conf /etc/nginx/conf.d
COPY ca/server-cert.pem /etc/nginx/conf.d/server-cert.pem
COPY ca/server-key.pem /etc/nginx/conf.d/server-key.pem

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 443