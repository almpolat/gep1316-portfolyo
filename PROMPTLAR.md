# Prompt Günlüğü ve YZ Beyanı

Kullanılan araç: Claude (Anthropic), claude.ai

Aşağıdaki istemleri sohbette aynen bu şekilde gönderdim.

| İstemim | YZ ne yaptı? | Ben ne yaptım? |
|---|---|---|
| Aşağıdaki notlarımı Markdown biçiminde bir README'ye dönüştür. Bir başlık, bir liste ve bir bağlantı olsun. Cümlelerimi değiştirme, yalnızca düzenle: [tanıtım, ders beklentisi ve "Kodlama ve YZ'nin mesleğimdeki yeri" notlarım] | Notlarımı başlıklara ayırdı, ilgi alanlarımı ve beklentilerimi listeye çevirdi, portfolyo sitemi bağlantı yaptı. Cümlelerime dokunmadı. Paragrafın 98 kelime olduğunu, ödevin 100–150 kelime istediğini söyledi. | Paragrafın sonuna "Bu derste Python'u öğrenerek bu tür araçları kendim yazabilmek istiyorum." cümlesini ekleyerek 108 kelimeye tamamladım. |
| Python'da kullanıcıdan adını ve doğum yılını alıp yaşını hesaplayan, kişiye özel bir karşılama mesajı yazan bir program yaz. Her satırı Türkçe yorumla açıkla. Ardından input() ve int() satırlarını, hiç kod bilmeyen birine anlatır gibi açıkla. | merhaba.py'yi her satırı yorumlu yazdı; input()'u "soru sorup cevabı bekleyen garson", int()'i "yazıyı sayıya çevirme" benzetmesiyle anlattı. Testte 2030 girilince yaşın −4 çıktığını ve harf girilince programın çöktüğünü gösterdi. | Programı çalıştırıp çıktının ekran görüntüsünü aldım. İki sorundan gelecek yıl sorununu düzeltmeye karar verdim. |
| Doğum yılı bu yıldan büyükse uyarı vermek istiyorum. Kodu yazma; hangi Python yapısını kullanmam gerektiğini bir ipucuyla anlat. | Kod yazmadan if/else kullanmam gerektiğini, karşılaştırmanın bu_yil satırından sonra gelmesi gerektiğini, ">" işaretini ve girinti kuralını ipucu olarak verdi. | Değişikliği kurarken koşulda ">" işaretini ve "Uyarı: Doğum yılı gelecekte olamaz!" mesajını seçtim; YZ seçimlerimi koda yerleştirdi. Harf kontrolünü (try/except) bu sürümde eklememeye karar verdim. 2004, 2026, 2027 ve 2030 ile test ettim. |
| Şu değişiklik için kısa ve anlamlı bir Türkçe commit mesajı öner: merhaba.py dosyasına, doğum yılı bu yıldan büyük girilirse "Doğum yılı gelecekte olamaz!" uyarısı veren bir if/else kontrolü ekledim. | Üç commit mesajı önerdi. | En kısa olan "Gelecek doğum yılı için uyarı eklendi" mesajını seçtim. |

## Bilinen sınır

Doğum yılına harf (ör. "abc") girilirse program `ValueError` hatasıyla kapanıyor. Bu kontrolü bilerek bu sürüme eklemedim.

## YZ Kullanım Beyan Formu

| Alan | Yanıtım |
|---|---|
| Kullanılan YZ aracı/araçları | Claude (Anthropic), claude.ai |
| Kullanma amacı | README notlarını Markdown'a dönüştürme, merhaba.py programını yazdırma ve açıklatma, kendi değişikliğim için ipucu alma, commit mesajı önerisi, depoya yükleme |
| Kontrol ve sorumluluk | Yapay zekâ tarafından üretilen içeriği gözden geçirdiğimi, gerekli düzeltmeleri yaptığımı ve teslim ettiğim çalışmanın doğruluğundan ve akademik dürüstlüğünden sorumlu olduğumu beyan ederim. |
| Öğrencinin adı-soyadı | Alimert Polat |
| Tarih ve İmza | 17.11.2026 – Alimert Polat |

## Kaynak

Anthropic. (2026). *Claude* [Büyük dil modeli]. https://claude.ai
