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
                await  context.bot.send_message(chat_id = context._chat_id, text= "yaaaaay\nApartments available\nRemoved the job automatically\nCounter is at:" + " " + str(checker.counter))
        elif checker.status == "No apartments available":        
                if checker.counter >= 200:
                    await  context.bot.send_message(chat_id = context._chat_id, text="Sorry nothing is availble\nchecked for 6 hours\nCounter is at" + " " + str(checker.counter))
                    checker.counter = 0
        




async def go(update: Update, context: CallbackContext):
    # chat_id = context._chat_id
    # job_queue = Application.job_queue
    job = context.chat_data.get('solution')
    if job:
          await context.bot.send_message(chat_id = context._chat_id, text="job already running..")
    else:
        await  context.bot.send_message(chat_id = context._chat_id, text="job started for the first time")
        job = context.chat_data['solution'] = context.job_queue.run_repeating(solution, interval=90, first=0, name = "solution", chat_id=context._chat_id)
    print("go started")



async def job(update: Update, context: CallbackContext) -> None:
        checker.thejob()
        if checker.status == "apartments available":
            await  context.bot.send_message(chat_id = context._chat_id, text= "yaaaay!\nApartments are availble\nCounter is at:" + " " + str(checker.counter))
        elif checker.status == "No apartments available":
            await  context.bot.send_message(chat_id = context._chat_id, text= "Sorry nothing is availble\nCounter is at:" + " " + str(checker.counter))



async def look(update: Update, context: CallbackContext) -> None:

        if checker.status == "apartments available":
            await  context.bot.send_message(chat_id = context._chat_id, text= "yaaaay!\nApartments are availble\nCounter is at:" + " " + str(checker.counter))
        elif checker.status == "No apartments available":
            await  context.bot.send_message(chat_id = context._chat_id, text= "Sorry nothing is availble\nCounter is at:" + " " + str(checker.counter))



def main() -> None:

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("fetch", job))
    application.add_handler(CommandHandler("scout" , go))
    application.add_handler(CommandHandler("look" , look))


    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)




if __name__ == "__main__":
    main()



        
