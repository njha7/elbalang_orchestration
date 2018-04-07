FROM python:alpine
RUN pip install flask
COPY src /src/
WORKDIR /src/elbalang
CMD python3 setup.py install
EXPOSE 5000
ENTRYPOINT [ "python", "/src/app.py" ]