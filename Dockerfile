FROM ubuntu:trusty

MAINTAINER FTG-Reversal

ENV PATH $PATH:/usr/local/app/bin

RUN apt-get -y update && apt-get -y upgrade && \
    apt-get -y install curl wget unzip build-essential git libgtk2.0-dev \
                       language-pack-ja-base language-pack-ja vim software-properties-common ruby && \
    add-apt-repository -y ppa:mc3man/trusty-media && apt-get -y update && apt-get -y install ffmpeg && \
    apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*
ENV PATH /opt/conda/bin:$PATH
ENV LANG C.UTF-8
ENV MINICONDA Miniconda3-latest-Linux-x86_64.sh
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget -q https://repo.continuum.io/miniconda/$MINICONDA && \
    bash /$MINICONDA -b -p /opt/conda && \
    conda install -y conda && \
    conda update -y conda && \
    conda install -y flask && \
    conda install -y -c https://conda.binstar.org/menpo opencv3 && \
    rm -rf /$MINICONDA

ADD . /usr/local/app
WORKDIR /usr/local/app

CMD /usr/local/app/bin/server
