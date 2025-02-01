from django.core.management.base import BaseCommand
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
import requests,os
from dotenv import load_dotenv



load_dotenv()


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_URL = "http://localhost:8000/api/v1/platos/"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("¡Hola! Usa /platos para ver la lista de platos.")

async def listar_platos(update: Update, context: CallbackContext):
    response = requests.get(API_URL)
    data = response.json()

    if not data:
        await update.message.reply_text("No hay platos disponibles.")
        return

    message = "🍽 Lista de platos:\n"
    for plato in data:
        message += f"➡️ {plato['name']} (Ingredientes: {len(plato['ingredients'])})\n"

    await update.message.reply_text(message)

class Command(BaseCommand):
    help = "Inicia el bot de Telegram"

    def handle(self, *args, **options):
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("platos", listar_platos))

        self.stdout.write(self.style.SUCCESS("✅ Bot de Telegram iniciado"))
        app.run_polling()
