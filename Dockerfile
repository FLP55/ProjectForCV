FROM python:3.9-slim-buster
WORKDIR /tests_project/
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apk add chromium-chromedriver
RUN apk add chromium
COPY . .
CMD python -m pytest -s --alluredir=allure_report/ /tests_project/tests/