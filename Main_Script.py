import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging ayarları
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Botun başlangıç durumu (Sanal İşlem Modu)
bot_state = {
    "is_running": False,
    "virtual_capital": 15000.0,
    "mode": "SANAL İŞLEM"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_text = (
        "🤖 *BIST AI BOT*'a hoş geldiniz!\n\n"
        "Bu bot yalnızca **SANAL İŞLEM** amaçlıdır. Gerçek para veya Midas API bağlantısı içermez.\n\n"
        "Kullanılabilir komutlar:\n"
        "/start - Karşılama mesajı\n"
        "/durum - Bot durumunu ve sanal sermayeyi gösterir\n"
        "/baslat - Sanal işlem modunu başlatır\n"
        "/durdur - Botu durdurur\n"
        "/portfoy - Sanal portföyü gösterir\n"
        "/sinyaller - BIST sinyallerini kontrol eder\n"
        "/bugun - Bugünkü sanal işlem özetini gösterir\n"
        "/help - Komut listesini gösterir"
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")

async def durum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    status_str = "ÇALIŞIYOR" if bot_state["is_running"] else "DURDURULDU"
    status_text = (
        "🤖 *BIST AI BOT*\n"
        f"Durum: {status_str}\n"
        f"Mod: {bot_state['mode']}\n"
        f"Sanal sermaye: {bot_state['virtual_capital']:,.2f} TL"
    )
    await update.message.reply_text(status_text, parse_mode="Markdown")

async def baslat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    bot_state["is_running"] = True
    await update.message.reply_text("Sanal işlem modu başlatıldı 🚀")

async def durdur(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    bot_state["is_running"] = False
    await update.message.reply_text("Bot durduruldu ⏹️")

async def portfoy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    portfolio_text = (
        "📊 *Sanal Portföy*\n\n"
        f"Nakit: {bot_state['virtual_capital']:,.2f} TL\n"
        "Hisse Senetleri: Henüz açık pozisyon bulunmuyor."
    )
    await update.message.reply_text(portfolio_text, parse_mode="Markdown")

async def sinyaller(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("BIST veri bağlantısı henüz kurulmadı 📡")

async def bugun(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    summary_text = (
        "📅 *Bugünkü Sanal İşlem Özeti*\n\n"
        "Bugün gerçekleşen işlem bulunmuyor."
    )
    await update.message.reply_text(summary_text, parse_mode="Markdown")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "📋 *BIST AI BOT Komutları*\n\n"
        "/start - Botu karşılar\n"
        "/durum - Bot durumunu gösterir\n"
        "/baslat - Sanal işlemi başlatır\n"
        "/durdur - Botu durdurur\n"
        "/portfoy - Sanal portföyü gösterir\n"
        "/sinyaller - BIST veri durumunu gösterir\n"
        "/bugun - Günlük özeti gösterir\n"
        "/help - Yardım menüsü"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

def main() -> None:
    # Token kontrolü
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError(
            "HATA: TELEGRAM_BOT_TOKEN ortam değişkeni bulunamadı! "
            "Lütfen Railway Variables bölümünden token tanımladığınızdan emin olun."
        )

    # Uygulama oluşturucu (python-telegram-bot v21+)
    application = ApplicationBuilder().token(token).build()

    # Komut yönlendiricileri
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("durum", durum))
    application.add_handler(CommandHandler("baslat", baslat))
    application.add_handler(CommandHandler("durdur", durdur))
    application.add_handler(CommandHandler("portfoy", portfoy))
    application.add_handler(CommandHandler("sinyaller", sinyaller))
    application.add_handler(CommandHandler("bugun", bugun))
    application.add_handler(CommandHandler("help", help_command))

    logger.info("BIST AI BOT başlatılıyor (Polling)...")
    application.run_polling()

if __name__ == "__main__":
    main()