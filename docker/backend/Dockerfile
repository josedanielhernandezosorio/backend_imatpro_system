# pull official base image
FROM python:3.9.6-alpine

# set work directory
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
RUN mkdir -p /home/app
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# copy file
COPY ../../requirements.txt .
COPY backend_imatpro_system/ .
COPY com/ .
COPY config/ .
COPY logs/ .
COPY static/ .
COPY manage.py .
COPY docker/backend/entrypoint.sh .

# install psycopg2 dependencies
RUN apk update && \
        apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy entrypoint.sh
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

# chown all the files to the app user
RUN chown -R app:app .

# change to the app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
