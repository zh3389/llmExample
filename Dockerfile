FROM python:3.8-slim
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 7860

# CMD [ "uvicorn", "app:gui", "--host", "0.0.0.0", "--port", "7860", "--reload" ]
CMD [ "python", "-m", "gui" ]
