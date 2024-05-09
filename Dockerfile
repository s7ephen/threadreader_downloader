FROM debian:buster
MAINTAINER s7ephen
RUN apt-get update
RUN apt-get install -y python2 python-dev python-pip build-essential swig git 
RUN apt-get install -y python-lxml ffmpeg
RUN pip install requests

VOLUME ["/workdir"]
WORKDIR /workdir/

COPY ["code/","/root/"]
#RUN tar xvfz /root/twitter-media-downloader-v1.13.2-linux-amd64.tar.gz
RUN chmod -R a+x /root/
RUN export PATH=$PATH:/root/
#ENTRYPOINT ["/root/download_threadreaderapp_thread.py"]
CMD ["/root/download_threadreaderapp_thread.py"]
