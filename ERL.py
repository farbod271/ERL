
from telegram import ForceReply, Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import checker
import varibles
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)



# global active
# active = True
application = Application.builder().token(varibles.TOKEN).build()

# job_queue = application.job_queue

# async def thejob(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#         url  = "https://www.erl.de/wp-json/kundenportal/v1/onoffice/get-stammobjekt-free-apartments?id=573"

#         # counter = 0
#         response = urlopen(url)
#         data_json = json.loads(response.read())
#         job = context.job
#         chat_id = update.message.chat_id

#         try:
#                 if (data_json["success"] == True) and data_json["apartmentsAvailable"]["0"] == 0 and (data_json["apartmentsAvailable"]["1"] == 0) and (data_json["apartmentsAvailable"]["2"] == 0) and (data_json["apartmentsAvailable"]["3"] ==280):
#                         # counter += 1
#                         # if counter > 60:
#                         # await context.bot.send_message(chat_id=chat_id, text="No apartments available")
#                         print("No apartments available")
#                                 # counter = 0
#                 else:
#                         # await context.bot.send_message(chat_id=chat_id, text="No apartments available")
#                         print("No apartments available")
#         except:
#                 print("Error")
#                 # active = True
#         # await context.bot.send_message(chat_id=chat_id, text="jobbing!")
#         print("Bot started")



# job_queue.run_repeating(thejob, interval=5, first=0)






async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )
    await  context.bot.send_message(chat_id = context._chat_id, text="its working")



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def solution(update: Update, context: ContextTypes.DEFAULT_TYPE):
        checker.thejob()
        # if checker.counter > 1:
        #    
        await  context.bot.send_message(chat_id = context._chat_id, text=checker.status)


def main() -> None:

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("job", solution))
    # solution(update, context)
    application.add_handler(MessageHandler(filters.CHAT , solution))





    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)




if __name__ == "__main__":
    main()



        
