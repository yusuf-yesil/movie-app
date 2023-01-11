# movie-app
# Film Tanıtım Sayfası

Bu proje, Django kullanılarak geliştirilen bir film tanıtım sayfasıdır. 
Kullanıcılar filmlerin detaylarını görüntüleyebilir. Şuanda hala kendimi geliştirdiğim için 
daha fazla ayrıntı ekleyemedim ama ilerleyen zamanlarda bu projeyi geliştirmeyi hedeflemekteyim.
Projem son halini aldığında yan menü işlevselleşmiş, oyuncuların bilgilerine erişebilir ve 
filmlere yapılan yorumları okulunabilir bir durumda olmasını düşünüyorum.

## Teknolojiler
- Django
- Python
- HTML/CSS
- Bootstrap
- SQLite

## Kurulum
Projeyi kurmak için aşağıdaki adımları izleyin:
1. Repository'i klonlayın veya indirin.
2. Proje dizinine gidin ve `pip install -r requirements.txt` komutunu çalıştırarak gerekli paketleri yükleyin.
3. `python manage.py makemigrations` ve `python manage.py migrate` komutlarını çalıştırarak veritabanını oluşturun.
4. `python manage.py runserver` komutunu çalıştırarak projeyi çalıştırın.
5. Tarayıcınızda `http://127.0.0.1:8000/` adresine gidin ve projeyi kullanmaya başlayın.

## Kullanım
1. Anasayfada ve filmler bölümündeki yer alan filmleri inceleyebilirsiniz.
2. Film detay sayfasına giderek filmle ilgili daha fazla bilgiye ulaşabilirsiniz.
