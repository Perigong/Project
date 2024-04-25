import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
vk_session = vk_api.VkApi(token = "YOUR_TOKEN")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

def send_some_message(id, some_text):
    vk_session.method("messages.send", {"user_id":id, "message":some_text, "random_id":0})

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text.lower()
            id = event.user_id()
            if message == "hi":
                send_some_message(id, "Hi friend!")