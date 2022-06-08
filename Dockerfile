FROM ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y tzdata

RUN unlink /etc/localtime
RUN ln -s /usr/share/zoneinfo/America/Phoenix /etc/localtime

RUN apt-get update -y \
    && apt-get install -y \
    python2.7.x \
    python-pip \
    python-tk \
    sqlite3 \
    systemd \
    openbox \
    tigervnc-standalone-server \
    supervisor \
    xterm \
    git \
    libssl-dev \
    python3-dev \
    python3-pip \
    python3-numpy \
    && rm -rf /var/lib/apt/lists/*

COPY menu.xml /etc/xdg/openbox/
COPY supervisord.conf /etc/supervisor/conf.d/xxx.conf
COPY . /fdlog/
RUN rm /etc/localtime && ln -s /usr/share/zoneinfo/America/Phoenix /etc/localtime
ENV PATH /home/user/app/bin /:$PATH

RUN groupadd --gid 1000 app && \
     useradd --home-dir /data --shell /bin/bash --uid 1000 --gid 1000 app && \
     mkdir -p /data && \
     chown app:app /data

RUN chown app:app -R /data/
RUN chown app:app -R /var/
RUN chown app:app -R /usr/
RUN chown app:app -R /fdlog/

USER 1000

ADD --chown=1000 https://github.com/novnc/noVNC/archive/refs/tags/v1.3.0.tar.gz /data/
RUN cd /data && tar -xvf v1.3.0.tar.gz
RUN git clone https://github.com/novnc/websockify /data/noVNC-1.3.0/utils/websockify

EXPOSE 5900
EXPOSE 6080
USER 0

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
