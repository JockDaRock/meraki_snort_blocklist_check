FROM python:alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY meraki_site_check.py .meraki_site_check.py

CMD ["python", "meraki_site_check.py"]