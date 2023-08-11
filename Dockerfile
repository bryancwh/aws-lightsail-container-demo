FROM python:3
COPY . /ToDo
RUN pip install flask
RUN pip install flask_sqlalchemy
RUN pip install pymysql
EXPOSE 8080
CMD [ "python", "./ToDo/todo.py"]