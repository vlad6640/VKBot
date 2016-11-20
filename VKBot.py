import vk
import time
import datetime
import platform

print('VKBot')

session = vk.Session('e838a9ea9c2eb21cdb69af65422c4871d8191d88a7d382376b69b8b526c66e0f64b71184b6610b27dab17')

api = vk.API(session)

while(True):
    messages = api.messages.get()
    commands = ['help', 'weather']
    messages = [(m['uid'], m['mid'], m['body'])
                for m in messages[1:] if m['body'] in commands and m['read_state'] == 0]
    for m in messages:
        user_id = m[0]
        message_id = m[1]
        comand = m[2]

        date_time_string = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
        if comand == 'help':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>VKBot v0.1 \n>Разработал vlad6640')

        if comand == 'weather':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>Погода отличная!')

        ids = ', '.join([str(m[1]) for m in messages])

        if ids:
            api.messages.markAsRead(message_ids=ids)

        time.sleep(3)


print(platform.system())
print(platform.platform())
print(platform.machine())
print(platform.version())
print(platform.processor())