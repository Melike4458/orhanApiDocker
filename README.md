# Flask Tabanlı Kullanıcı Yönetim API'si

Bu proje, Flask tabanlı bir RESTful API uygulamasıdır. Uygulama, kullanıcı bilgilerini yönetmek için bir dizi CRUD işlemi sunar ve Dockerize edilmiştir. Docker ve Docker Compose kullanarak kolayca çalıştırabilirsiniz.


## Gereksinimler

- Docker (20.x veya üzeri)
- Docker Compose (v2.12.2 veya üzeri)
- cURL veya Postman (API isteklerini test etmek için)

## Proje kullanımı.
1. Projeyi github'dan lokale indirin.
   ```bash
   git clone https://github.com/Melike4458/orhanApiDocker
   ```

2. Proje klasörüne girin.
   ```bash
   cd orhanApiDocker/
   ```

3. Compose ile projeyi ayağa kaldırın.
   ```bash
   docker compose up -d
   ```


## Proje Ayaktamı?
1. En kolay yöntem tarayıcınız üzerinden GET isteği ile öğrenmiş olursunuz.
   ```bash
   http://localhost:5044
   **Response**: {"message": "Merhabalar!"}
   ```

2. curl ile GET isteği yaparak öğrenebilirsiniz.
   ```bash
   curl http://localhost:5044/
   ```

3. POSTMAN kullanarak öreğenebiliriz.
   Aşağıda verilen API fonksiyonları kısmında ki örnekler ile POSTMAN üzerinden istek yapılabilir.




## Kurulum ve Çalıştırma

## Docker Kurulumu
1. Sisteminizde docker kurulu olmalı:
   ```bash
   sudo apt-get update
   sudo apt-get install -y docker.io
   ```

## Docker Compose Kurulumu
1. docker-compose.yaml ile compese kullanımı için kurulu olmalı.
   ```bash
   sudo apt-get update
   sudo apt-get install -y docker.io
   ```

### Docker Image Oluşturma
1. Proje dizinine gidin:
   ```bash
   cd /path/to/your/project
   ```

2. Docker imajını oluşturun:
   ```bash
   docker build -t orhan_api .
   ```

### Docker Image Güncelleme
1. Proje dizinine gidin:
   ```bash
   cd /path/to/your/project
   ```

2. Güncellenmiş kodlarla yeniden imaj oluşturun:
   ```bash
   docker build -t orhan_api .
   ```

### Docker Container Çalıştırma
1. Konteyneri başlatın:
   ```bash
   docker run -d -p 5044:5044 -v $(pwd)/var:/var --name orhan_api orhan_api
   ```

2. Çalıştığını doğrulamak için:
   ```bash
   curl http://localhost:5044/
   ```

### Docker Container Durdurma
1. Konteyneri durdurun: 
   ```bash
   docker stop orhan_api
   ```
### Docker Container Silme
1. Konteyneri silin:
   ```bash
   docker rm -f orhan_api
   ```

## Docker Compose Kullanımı
1. Docker Compose ile konteyneri (docker-compose.yaml ile tüm servisleri tek sistem ile ayağa kaldırır) çalıştırın:
   ```bash
   docker-compose up -d
   ```

2. Çalıştığını doğrulamak için:
   ```bash
   curl http://localhost:5044/
   ```





## API Fonksiyonları

### 1. Home Sınıfı
Bu sınıf, uygulamanın temel çalışma durumunu kontrol etmek için basit bir mesaj döner.
- Endpoint: /
- HTTP Method: GET
- Örnek Cevap:
  {
    "message": "Merhabalar!"
  }

### 2. Users Sınıfı
Bu sınıf, kullanıcı bilgilerini yönetmek için çeşitli metodlar içerir.

#### a. get Metodu
- CSV dosyasındaki kullanıcı verilerini okur.
- Tüm kullanıcıları bir JSON formatında döner.
- Endpoint: /users
- HTTP Method: GET
- Örnek Cevap:
  {
    "data": [
      {"name": "Ali", "age": 25, "city": "Istanbul"},
      {"name": "Ayşe", "age": 30, "city": "Ankara"}
    ]
  }

#### b. post Metodu
- Yeni bir kullanıcıyı CSV dosyasına ekler.
- Endpoint: /users
- HTTP Method: POST
- Gerekli Parametreler: 
  {
    "name": "Fatma",
    "age": 28,
    "city": "Izmir"
  }
- Örnek Cevap:
  {
    "message": "Kayıt eklendi."
  }

#### c. delete Metodu
- Belirtilen kullanıcıyı CSV dosyasından siler.
- Endpoint: /users?name=<KullanıcıAdı>
- HTTP Method: DELETE
- Örnek Cevap:
  {
    "message": "Kayıt silindi."
  }

### 3. Cities Sınıfı
Bu sınıf, tüm kullanıcıların şehir bilgilerini döner.
- Endpoint: /cities
- HTTP Method: GET
- Örnek Cevap:
  {
    "data": [
      {"city": "Istanbul"},
      {"city": "Ankara"}
    ]
  }

### 4. Name Sınıfı
Belirli bir kullanıcıyı arar ve döner.
- Endpoint: /<string:name>
- HTTP Method: GET
- Örnek Cevap (Kullanıcı Bulundu):
  {
    "data": {
      "name": "Ali",
      "age": 25,
      "city": "Istanbul"
    }
  }
- Örnek Cevap (Kullanıcı Bulunamadı):
  {
    "message": "Bu isimde bir kayıt bulunamadı!"
  }

### 5. AddNumbers Sınıfı
Verilen sayıları toplar ve sonucu döner.
- Endpoint: /add_numbers?num=5&num=10
- HTTP Method: GET
- Örnek Cevap:
  {
    "result": 15
  }

### 6. MultiplyNumbers Sınıfı
İki sayıyı çarpar ve sonucu döner.
- Endpoint: /multiply_numbers?num1=5&num2=3
- HTTP Method: GET
- Örnek Cevap:
  {
    "result": 15
  }

## Test

### cURL Kullanımı
1. Örnek bir GET isteği:
   curl http://localhost:5044/users

2. Kullanıcı ekleme için POST isteği:
   curl -X POST -d "name=Fatma&age=28&city=Izmir" http://localhost:5044/users

### Postman Kullanımı
1. Postman'de yeni bir istek oluşturun.
2. Gerekli endpoint ve HTTP metodunu seçin.
3. Parametreleri ekleyerek isteği gönderin.

## Proje Yapısı
project/
├── orhanApi.py            # Flask uygulama dosyası
├── requirements.txt       # Bağımlılık dosyası
├── Dockerfile             # Docker yapılandırma dosyası
├── docker-compose.yaml    # Docker Compose yapılandırma dosyası
└── README.md              # Dokümantasyon dosyası
