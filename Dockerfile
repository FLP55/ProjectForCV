FROM python:3.9-alpine
WORKDIR /tests_project/
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apk add chromium-chromedriver
RUN apk add chromium
COPY . .
CMD docker run -d -p 4444:4444 selenium/standalone-chrome
# CMD python -m pytest -s --alluredir=allure_report/ /tests_project/tests/