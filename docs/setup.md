# Menjalankan Project

## Pertama kali

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install

## Setiap hari

venv\Scripts\activate
python -m tests.test_scraper