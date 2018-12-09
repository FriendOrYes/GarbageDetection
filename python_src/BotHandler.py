import requests
from PIL import Image
from io import BytesIO
import json

img_width, img_height = 256, 256
input_shape = (img_width, img_height, 3)

class BotHandler:
    def __init__(self, token):
        print("Create bot handler")
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        print("get update")
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def get_last_update(self):
        get_result = self.get_updates()
        print(type(get_result))

        if not get_result:
            return None

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

    def send_message(self, chat_id, text):
        print("send message")
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def getImageById(self, imageid):
        #https: // api.telegram.org / bot < bot_token > / getFile?file_id = the_file_id
        method = "getFile"
        params = {'file_id': imageid}

        print(self.api_url + method + str(params))

        resp = requests.get(self.api_url + method, params)

        print(resp.text)

        if not resp.text:
            return None

        s = resp.text
        json_acceptable_string = s.replace("'", "\"")
        text = json.loads(json_acceptable_string)

        if "result" not in text:
            return None

        print("text:  ", text)
        print(type(text))
        file = text["result"]["file_path"]

        print("type : ", type(file))

        print("file: ", file)
        fileurl = "https://api.telegram.org/file/bot{}/".format(self.token)
        response = requests.get(fileurl + file)

        print("type: ", type(response.text))

        if not response.status_code == 200:
            return None

        img = Image.open(BytesIO(response.content))

        size = 256, 256

        img = img.resize(size, Image.ANTIALIAS)

        return img
