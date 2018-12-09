import datetime
import requests
import load
import BotHandler

token = "741817521:AAGBN8Gke3513NXNpr6backtPuKju7QC-Jw"
greet_bot = BotHandler.BotHandler(token)
greetings = ('здравствуй', 'привет', 'ку', 'здорово')
now = datetime.datetime.now()


def main():
    print("start")
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        print("in while")
        print(greet_bot.get_updates(new_offset))
        last_update = greet_bot.get_last_update()

        print(last_update)
        print("type: ", type(last_update))

        last_update_id = ""
        last_chat_text = ""
        last_chat_id = ""

        if not last_update:
            continue

        if "update_id" in last_update:
            last_update_id = last_update['update_id']

        if not "message" in last_update:
            continue

        if "message" in last_update and "text" in last_update['message']:
            last_chat_text = last_update['message']['text']

        if "chat" in last_update['message']:
            if 'id' in last_update['message']['chat']:
                last_chat_id = last_update['message']['chat']['id']

            if 'first_name' in last_update['message']['chat']:
                last_chat_name = last_update['message']['chat']['first_name']

        avatarId = ""
        photo = ""
        if "photo" in last_update['message']:
            photo = last_update['message']['photo']

        print("last_update_id: ", last_update_id)
        print("day: ", now.day)
        print("today: ", today)
        print("last_chat_text: ", last_chat_text)
        print("imageId: ", photo)
        print("len(photo): ", len(photo))
        if len(photo) > 1:
            if 'file_id' in photo[1]:
                imageId = photo[1]['file_id']

                print("imageId: ", imageId)
                image = greet_bot.getImageById(imageId)
                info = load.getImageInfo(image)
                if info:
                    greet_bot.send_message(last_chat_id, 'Your Image is: {}'.format(info))

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
            today += 1

        new_offset = int(last_update_id) + 1

main()
