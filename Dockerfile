FROM mcr.microsoft.com/playwright:v1.29.1-focal

ARG CACHEBUST=1

RUN apt update
RUN apt install ffmpeg libsm6 libxext6  -y
RUN apt install python3-pip -y
RUN apt install libevent-2.1-7
RUN apt install libenchant-2-2

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install playwright
RUN playwright install

RUN pip install --upgrade google-api-python-client
RUN pip install --upgrade google-auth-oauthlib google-auth-httplib2

CMD ["python3", "bot.py"]
