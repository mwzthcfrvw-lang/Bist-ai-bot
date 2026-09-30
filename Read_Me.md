# BIST AI BOT

BIST AI BOT, Telegram üzerinden kontrol edilen, yapay zeka altyapısına hazırlık aşamasındaki bir sanal işlem takip botudur.

## ⚠️ Önemli Güvenlik ve Sürüm Notu
- **Yalnızca Sanal İşlem:** Bu sürüm tamamen simülasyon amaçlıdır. 
- **Gerçek Para Yoktur:** Sistemde gerçek para, yatırım hesabı veya Midas API bağlantısı **kesinlikle bulunmamaktadır**.
- **Gizlilik:** Bot token bilgilerinizi hiçbir şekilde GitHub deposuna yüklemeyin.

## Railway Kurulum Adımları

1. Projeyi Railway'e GitHub üzerinden bağlayın.
2. Railway proje panelinde **Variables** sekmesine gidin.
3. Yeni bir değişken ekleyin:
   - **Key:** `TELEGRAM_BOT_TOKEN`
   - **Value:** BotFather üzerinden aldığınız Telegram Bot Token değeriniz
4. Railway otomatik olarak `requirements.txt` üzerinden bağımlılıkları kuracak ve `Procfile` dosyasındaki komut ile botunuzu `worker` modunda çalıştıracaktır.