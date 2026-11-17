# merhaba.py - Kullanıcının adını ve doğum yılını alıp yaşını hesaplayan program

# Bugünün tarihini öğrenebilmek için datetime modülünü programa ekliyoruz
from datetime import date

# Kullanıcıdan adını istiyoruz ve "ad" adlı değişkene kaydediyoruz
ad = input("Adınız nedir? ")

# Kullanıcıdan doğum yılını istiyoruz; gelen metni int() ile tam sayıya çeviriyoruz
dogum_yili = int(input("Doğum yılınız nedir? "))

# Bilgisayarın saatinden içinde bulunduğumuz yılı alıyoruz (ör. 2026)
bu_yil = date.today().year

# Bu yıldan doğum yılını çıkararak yaşı hesaplıyoruz
yas = bu_yil - dogum_yili

# Kişiye özel karşılama mesajını ekrana yazdırıyoruz
print(f"Merhaba {ad}! GEP1316 dersine hoş geldin.")

# Hesaplanan yaşı ekrana yazdırıyoruz
print(f"Bu yıl {yas} yaşına giriyorsun.")
