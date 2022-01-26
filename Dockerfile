FROM baseimage-python


WORKDIR /tmp/

LABEL maintainer="blueprintcode@outlook.com"
ENV PYTHONPATH="${PYTHONPATH}:/data/www/backend/"
COPY ./requirements.txt .

RUN mkdir /data \
   && mkdir /data/service \
	&& mkdir /data/www \
   && mkdir /data/www/backend \
   && mkdir /data/www/backend/logs \
   && chmod 775 /data/service \
	&& apt-get update \
	&& apt-get install -y nginx \
	&& python -m pip install -r requirements.txt \
	&& groupmod --gid 80 --new-name www www-data \
	&& usermod --uid 80 --home /data/www --gid 80 --login www --shell /bin/bash --comment www www-data \
	&& ln -s /etc/nginx/sites-available/api /etc/nginx/sites-enabled \
	&& rm /etc/nginx/sites-enabled/default

COPY api /etc/nginx/sites-available/api
COPY nginx.conf /etc/nginx/nginx.conf
COPY backend/ /data/www/backend
COPY entrypoint.sh .

EXPOSE 5000

ENTRYPOINT ["/bin/bash","entrypoint.sh"]