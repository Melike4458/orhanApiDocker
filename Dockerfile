# Base image
FROM python:3.10.12-slim

# Çalışma dizini oluştur
WORKDIR /app

# Bağımlılık dosyalarını kopyala
COPY requirements.txt requirements.txt

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Log ve veri dizinlerini oluştur
RUN mkdir -p /var/log/orhanApi /var/lib/orhanApi

# Uygulama dosyasını kopyala
COPY orhanApi.py orhanApi.py

# Container çalıştırma komutu
CMD ["python3", "orhanApi.py"]
