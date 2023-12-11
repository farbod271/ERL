from telegram import Update, TelegramObject
from telegram.ext import Application, CommandHandler, ContextTypes,CallbackContext
import checker
import varibles
import logging
import names
# from datetime import datetime



logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)
application = Application.builder().token(varibles.TOKEN).build()


# async def warning():
#     updater = application.updater
#     await updater.initialize()
#     await updater.bot.send_message(chat_id = , text="bot restarted due to maintenance")
    # application.bot.send_message(chat_id = , text="bot restarted due to maintenance")
# warning()





async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # user = update.effective_user
    # await update.message.reply_html(
    #     rf"Hi {user.mention_html()}!",
    #     reply_markup=ForceReply(selective=True),
    # )
    await  context.bot.send_message(chat_id = context._chat_id, text="Hi the bot is working")
    await  context.bot.send_message(chat_id = context._chat_id, text="Use /scout for auto check\nUse /fetch to get live data\nUse /look when scout is active to check the last status of the apartments\nUse /stop_scout to stop the bot from scouting for you")




async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")




async def solution(context: CallbackContext) -> None:
        checker.thejob()
        print("SOLUTION STARTED")
        
        if checker.status == "apartments available":
                job = context.bot_data.get('solution')
                job.schedule_removal()  # remove the repeating job from the job queue
                del context.bot_data['solution']
                [await context.bot.send_message(chat_id=id, text="yaaaaay\nApartments available\nRemoved the job automatically\nCounter is at:" + " " + str(checker.counter)) for id in names.scout_ids]
                # await  context.bot.send_message(chat_id = for name in names.list , text= "yaaaaay\nApartments available\nRemoved the job automatically\nCounter is at:" + " " + str(checker.counter))
        elif checker.status == "No apartments available":        
                if checker.counter >= 320:
                    await  context.bot.send_message(chat_id = context._chat_id, text="Sorry nothing is availble\nchecked for 8 hours\nCounter is at" + " " + str(checker.counter))
                    checker.counter = 0
        




async def go(update: Update, context: CallbackContext):
    # chat_id = context._chat_id
    # job_queue = Application.job_queue
    # print(names.scout_ids)
    # print(names.scout_names)
    # print(update.effective_chat.username)
    # print(names.scout_names)



    job = context.bot_data.get('solution')
    if job and update.message.chat_id not in names.scout_ids:
          names.scout_ids.add(update.message.chat_id)
          names.scout_names.add(str(update.effective_chat.username))
        #   print(context._chat_id)

          await context.bot.send_message(chat_id = context._chat_id, text="bot is scouting for you now. it will let you know if an apartment is available")
        #   print(context, names.scout_names)
          the_names = str(names.scout_names)
          file_path = "scouters.txt"
          with open(file_path, 'w') as file:
            file.write(the_names)
    elif job and update.message.chat_id in names.scout_ids:
        await context.bot.send_message(chat_id = context._chat_id, text="bot is already scouting for you")
    else:
        names.scout_ids.add(update.message.chat_id)
        names.scout_names.add(str(update.effective_chat.username))
        the_names = str(names.scout_names)
        file_path = "scouters.txt"
        with open(file_path, 'w') as file:
            file.write(the_names)
        await  context.bot.send_message(chat_id = context._chat_id, text="job started for the first time")
        job = context.bot_data['solution'] = context.job_queue.run_repeating(solution, interval=90, first=0, name = "solution", chat_id=context._chat_id)
    print("go started")



async def job(update: Update, context: CallbackContext) -> None:
        # print(update.effective_chat.id)
        if update.effective_chat.id not in names.fetch_ids:
            names.fetch_ids[update.effective_chat.id] = int(1)
            names.fetch_names[update.effective_chat.username] = int(1)

        else:
            names.fetch_names[update.effective_chat.username] += 1
            names.fetch_ids[update.effective_chat.id] += 1
            # print(update.effective_chat.id)

        # print(names.dict)
        text_to_save = str(names.fetch_names)
        file_path = "namess.txt"
        with open(file_path, 'w') as file:
            file.write(text_to_save)
        # print(f"String saved to '{file_path}'")

        if names.fetch_ids[update.effective_chat.id] <= 120:
            checker.notjob()
            if checker.status == "apartments available":
                await  context.bot.send_message(chat_id = context._chat_id, text= "yaaaay!\nApartments are availble\nCounter is at:" + " " + str(checker.counter))
            elif checker.status == "No apartments available":
                await  context.bot.send_message(chat_id = context._chat_id, text= "Sorry nothing is availble\nCounter is at:" + " " + str(checker.counter))
        else:
            await  context.bot.send_message(chat_id = context._chat_id, text= "fuck off. you sent too many requests")



async def look(update: Update, context: CallbackContext) -> None:

        if checker.status == "apartments available":
            await  context.bot.send_message(chat_id = context._chat_id, text= "yaaaay!\nApartments are availble\nCounter is at:" + " " + str(checker.counter))
        elif checker.status == "No apartments available":
            await  context.bot.send_message(chat_id = context._chat_id, text= "Sorry nothing is availble\nCounter is at:" + " " + str(checker.counter))

async def stop(update: Update, context: CallbackContext):
     
        if update.message.chat_id in names.scout_ids:
            names.scout_ids.remove(update.message.chat_id)
            await  context.bot.send_message(chat_id = context._chat_id, text= "succesfully removed scouting for you")
            if not names.scout_ids:
                job = context.bot_data.get('solution')
                job.schedule_removal()  # remove the repeating job from the job queue
                del context.bot_data['solution']
                # print("looker stoped enirely")
        else:
            await  context.bot.send_message(chat_id = context._chat_id, text= "bot isnt scouting for you\nUse /scout first to start scouting")





def main() -> None:



    # on different commands - answer in Telegram
    # ContextTypes.DEFAULT_TYPE.bot.send_message(chat_id = ContextTypes.DEFAULT_TYPE. , text="bot restarted due to maintenance")
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("fetch", job))
    application.add_handler(CommandHandler("scout" , go))
    application.add_handler(CommandHandler("stop_scout" , stop))
    application.add_handler(CommandHandler("look" , look))


    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)





if __name__ == "__main__":
    main()





        
