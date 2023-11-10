from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes,CallbackContext
import checker
import varibles
import logging
# from datetime import datetime



logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


application = Application.builder().token(varibles.TOKEN).build()





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



# current_datetime = datetime.now()







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

async def solution(context: CallbackContext) -> None:
        checker.thejob()
        print("SOLUTION STARTED")
        if checker.status == "apartments available":
                job = context.chat_data.get('solution')
                job.schedule_removal()  # remove the repeating job from the job queue
                del context.chat_data['solution']
                await  context.bot.send_message(chat_id = context._chat_id, text= "removed! apartments available")
        elif checker.status == "No apartments available":        
                if checker.counter > 180:
                    await  context.bot.send_message(chat_id = context._chat_id, text="checked for 6 hours" + " " + str(checker.counter))
                    checker.counter = 0
        


async def go(update: Update, context: CallbackContext):
    # chat_id = context._chat_id
    # job_queue = Application.job_queue
    job = context.chat_data.get('solution')
    if job:
          await context.bot.send_message(chat_id = context._chat_id, text="job already running")
    else:
        await  context.bot.send_message(chat_id = context._chat_id, text="job started for the first time")
        job = context.chat_data['solution'] = context.job_queue.run_repeating(solution, interval=120, first=0, name = "solution", chat_id=context._chat_id)


    print("go started")

async def jobb(update: Update, context: CallbackContext) -> None:
        checker.thejob()
        # single_counter = 0
        await  context.bot.send_message(chat_id = context._chat_id, text= checker.status)


def main() -> None:

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("job", jobb))
    application.add_handler(CommandHandler("go" , go))


    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)




if __name__ == "__main__":
    main()



        
