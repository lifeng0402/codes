FROM python:3.10.4

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

WORKDIR /code

COPY ../requirements.txt /code/requirements.txt

RUN  python -m pip install --upgrade pip && pip install --no-cache-dir --upgrade -r /code/requirements.txt -i https://pypi.douban.com/simple/

COPY ./sc_app /code/sc_app

EXPOSE 8085

CMD ["uvicorn", "sc_app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8085"]



