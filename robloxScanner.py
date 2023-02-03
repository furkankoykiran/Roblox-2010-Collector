import requests

# Visit https://t.me/BotFather to get your bot Token.
Token = '8765498435:AAEwPQedsnMyJCLY3yteBMtmxqIj-AoOd5A'

# Visit https://web.telegram.org/k/ to get your group ID.
chat_id = -1866928477

# If your Telegram group is a supergroup, add -100 to the ID name.
    # Example: -1001866928477

def send_to_telegram(message):

    apiToken = Token
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chat_id, 'text': message})
        # print(response.text)
    except Exception as e:
        print(e)

id = int(input('Account ID to start check: '))
# You should enter here the start ID from which you will start checking accounts.
    # Example: 4017208

while True:
    try:
        url = f"https://users.roblox.com/v1/users/{id}"
        response = requests.get(url)
        data = response.json()
        try:
            date = data["created"][:10]
            name = data["name"]
            print(id,date,name)
            if len(name) > 19:
                if name.isalnum() and name.islower() and any(c.isdigit() for c in name):
                    send_to_telegram(f"https://www.roblox.com/users/{id}/profile\n\n{id}\n{date}\n{name}")
        except KeyError:
            pass
        id += 1
    except KeyboardInterrupt:
        print('Bot has been stopped.')
        break
    except:
        id += 1
        pass