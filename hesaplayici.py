# hesaplayici.py - Steam'de satılan bir oyunun geliştiriciye kalan net gelirini hesaplar

# Sabit oranlar: Türkiye'de genel KDV %20, Steam'in payı %30 (float tipinde)
KDV_ORANI = 0.20
STEAM_PAYI = 0.30

# Oyunun adını alıyoruz; input() her zaman metin (str) döndürür
oyun_adi = input("Oyunun adı: ")

# Fiyatı alıp float() ile ondalıklı sayıya çeviriyoruz (ör. 199.99)
fiyat = float(input("Oyunun fiyatı (TL): "))

# İndirim oranını alıp int() ile tam sayıya çeviriyoruz (ör. 25 = %25)
indirim_orani = int(input("İndirim oranı (%): "))

# Satış adedini alıp int() ile tam sayıya çeviriyoruz
satis_adedi = int(input("Satış adedi: "))

# Geliştirme maliyetini alıp float() ile ondalıklı sayıya çeviriyoruz
maliyet = float(input("Geliştirme maliyeti (TL): "))

# İndirimli fiyat: fiyattan indirim yüzdesi kadar düşüyoruz
indirimli_fiyat = fiyat * (1 - indirim_orani / 100)

# Brüt satış: indirimli fiyat ile satılan kopya sayısını çarpıyoruz
brut_satis = indirimli_fiyat * satis_adedi

# Steam fiyatlarına KDV dahildir; KDV'yi ayırarak KDV hariç geliri buluyoruz
kdv_haric = brut_satis * (1 - KDV_ORANI)

# Steam'in payını KDV hariç gelir üzerinden hesaplıyoruz
steam_kesintisi = kdv_haric * STEAM_PAYI

# Geliştiriciye kalan net gelir: KDV hariç gelirden Steam payını çıkarıyoruz
net_gelir = kdv_haric - steam_kesintisi

# Karşılaştırma operatörü (>=) ile maliyetin karşılanıp karşılanmadığını buluyoruz (bool)
maliyet_karsilandi = net_gelir >= maliyet

# Sonuçları f-string ile, binlik ayraçlı ve 2 ondalıklı biçimde yazdırıyoruz
print(f"\n--- {oyun_adi} için gelir raporu ---")
print(f"İndirimli fiyat     : {indirimli_fiyat:,.2f} TL")
print(f"Brüt satış          : {brut_satis:,.2f} TL")
print(f"KDV hariç gelir     : {kdv_haric:,.2f} TL")
print(f"Steam payı (%30)    : {steam_kesintisi:,.2f} TL")
print(f"Net gelir           : {net_gelir:,.2f} TL")
print(f"Maliyet karşılandı mı? {maliyet_karsilandi}")
