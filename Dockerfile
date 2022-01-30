FROM python:3.9-alpine3.14

WORKDIR /home/app

COPY . .
RUN addgroup -S guppi && adduser -S guppi_user -G guppi
RUN chown guppi_user:guppi -R /home/app
USER guppi_user
RUN pip install --no-cache-dir -r requirements.txt
RUN ln -s /usr/local/bin/python /bin

HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost:5001/about || exit 1

EXPOSE 5001

ENTRYPOINT ["/usr/local/bin/python"]
CMD [ "./app.py" ]