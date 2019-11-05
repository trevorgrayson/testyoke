FROM python:3.7-alpine

ADD . /
RUN pip install -r requirements.txt

EXPOSE 7357

ENTRYPOINT ["python"]
CMD ["-m", "testyoke.server"]

