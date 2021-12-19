FROM python:3.9-alpine3.14

WORKDIR /home/app

COPY requirements.txt ./
RUN useradd -ms /bin/bash guppi-user
RUN chown guppi-user:guppi-user -R /home/app
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER guppi-user

HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost:5001/about || exit 1

EXPOSE 5001

ENTRYPOINT ["/bin/python"]
CMD [ "./app.py" ]