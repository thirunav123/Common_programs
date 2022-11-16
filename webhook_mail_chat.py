
import requests,json
url="https://chat.googleapis.com/v1/spaces/AAAAlSEUKwQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=FlYMlmsUUdybse7uYiu8ruZbaiX5vqq-0ywI5KPeK2c%3D"

temp_data = f'<font color=\"#00ff00\"><i><b>Machine Breakdown Alert!</b></i>\n'\
            f'<b>Production Station : </b>STN-10\n'
data_dir = {"cards": [{"sections":[{"widgets":[{"textParagraph":{ 'text':f'{temp_data}'}}]}]}]}
# data = {'text':"Hi"}
r = requests.post(url, data=json.dumps(data_dir))#, headers={'Content-Type': 'application/json'})
