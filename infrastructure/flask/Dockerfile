FROM python:alpine
RUN pip install flask
RUN pip install --upgrade google-cloud-storage
COPY src /src/
ENV GOOGLE_APPLICATION_CREDENTIALS /src/ElbaOrchestration-e2637482b066.json
ENV INPUT_BUCKET elba-experiments
ENV OUTPUT_BUCKET elba-results
WORKDIR /src/elbalang
RUN python3 setup.py install
EXPOSE 5000
ENTRYPOINT [ "python", "/src/app.py" ]