import requests
import time
import dotenv
import os
from bs4 import BeautifulSoup
from dhooks import Webhook, Embed

dotenv.load_dotenv()

discord_webhook_url = os.environ['WEBDIP_DISCORD_WEBHOOK_URL']
hook = Webhook(discord_webhook_url)

game_id = os.environ['WEBDIP_GAME_ID']
points_icon = 'https://webdiplomacy.net/images/icons/points.png'
base_url =  'https://webdiplomacy.net'
game_url = '{}/board.php?gameID={}'.format(base_url, game_id)

last_game_date = ""

while True:
    r = requests.get(game_url)
    soup = BeautifulSoup(r.text, 'html.parser')

    game_date = soup.find_all('span', class_='gameDate')[0].string

    if not last_game_date == game_date:
        last_game_date == game_date

        game_name = soup.find_all('span', class_='gameName')[0].string

        embed = Embed(
            description=game_name,
            color=0x006699,
            timestamp='now'
            )

        time_remain_span = soup.find_all('span', class_='timeremaining')[0]
        unixtime = int(time_remain_span.get('unixtime'))
        unixtimefrom = int(time_remain_span.get('unixtimefrom'))
        seconds = unixtime - unixtimefrom
        hours = (seconds / 60) / 60
        embed.add_field(name='Next', value='{:.2f}hrs'.format(hours))

        big_map_img_url_postfix  = soup.find(id='LargeMapLink').get('href')
        big_map_img = '{}/{}'.format(base_url, big_map_img_url_postfix)
        embed.set_image(big_map_img)

        game_pot = soup.find_all('span', class_='gamePot')[0].get_text()
        footer_text = "Pot: {}, {}".format(game_pot, game_date)
        embed.set_footer(text=footer_text, icon_url=points_icon)

        hook.send(embed=embed)

    time.sleep(20)
