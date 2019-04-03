# webdiplomacy-info

[![Build Status](https://drone.jackharrhy.com/api/badges/jackharrhy/webdiplomacy-info/status.svg)](https://drone.jackharrhy.com/jackharrhy/webdiplomacy-info) [![](https://images.microbadger.com/badges/image/jackharrhy/webdiplomacy-info.svg)](https://microbadger.com/images/jackharrhy/webdiplomacy-info "Get your own image badge on microbadger.com")


<img src="https://i.imgur.com/JxH3CgJ.jpg" width="200">

## Run via Docker

```bash
docker run -d -e WEBDIP_GAME_ID="123456" \ 
   -e WEBDIP_DISCORD_WEBHOOK_URL="https://discordapp.com/api/webhooks/1234/abcdefg" \
   --name webdiplomacy-info jackharrhy/webdiplomacy-info
```

## Run without Docker

Requires Python 3 (tested only on 3.7)

```bash
cp .env.vidst .env
# edit the .env file with your editor of choice
pip install -r requirements.text
python remind.py
```
