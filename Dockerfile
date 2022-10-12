FROM snuspl/swpp:python3.9

RUN pip install django
RUN pip install pandas
RUN pip install coverage