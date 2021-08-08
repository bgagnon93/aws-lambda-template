FROM public.ecr.aws/lambda/python:3.8

COPY lambda_template/ ./
RUN pip install -r requirements.txt && \
    chmod -R 755 .

CMD [ "app.lambda_handler" ]