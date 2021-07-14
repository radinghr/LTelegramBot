FROM python:3.9
ENV TZ=Asia/Tehran
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y supervisor tzdata librdkafka-dev
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . ./
CMD ["sh", "/app/start_service.sh"]

