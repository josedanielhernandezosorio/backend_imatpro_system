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
COPY . .
COPY docker/backend/entrypoint.sh .

RUN rm -R virtual-backend-imatpro-system/
RUN rm -R .github/
RUN rm -R doc/
RUN rm -R docker/
RUN rm -R .git/
RUN rm -R .idea/
RUN rm db.sqlite3
RUN rm .gitignore
RUN rm pytest.ini
RUN rm README.md


# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

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
