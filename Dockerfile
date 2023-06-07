FROM selenium/standalone-chrome

FROM python:3.9-alpine
WORKDIR /tests_project/
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apk add chromium
RUN apk add chromium-chromedriver
COPY . .

# CMD python -m pytest -s --alluredir=allure_report/ /tests_project/gdotests/