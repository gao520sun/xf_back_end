FROM python:3.7
ENV REFRESHED_AT 2019-04-16
RUN mkdir -p /tmp/log

#设置工作目录
WORKDIR /mnt

COPY ./xfApp /mnt/xfApp

COPY requirements.txt /mnt/requirements.txt

RUN pip install -r requirements.txt

CMD ["python3","-m","xfApp.server"]
