FROM public.ecr.aws/docker/library/python:3.8.12-slim-buster
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.5.0 /lambda-adapter /opt/extensions/lambda-adapter
WORKDIR /var/task
COPY . ./
RUN python -m pip install -r requirements.txt
CMD ["gunicorn", "-b=:8080", "-w=1", "app:app"]
