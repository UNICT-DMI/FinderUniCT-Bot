# Finder-UniCT Bot
A Telegram bot for UNICT students that allows students to get to know each other semi-anonymously.

## How does it work?

This bot allows you to get straight to your telegram chat:

Send **'/start'** to start it, **'/help'** to see a list of commands.
Please note that the commands and their answers are in Italian.

---

## How to create a Telegram bot and get its token
To start testing this bot you need to get a Telegram Bot's token:
- Go to Telegram and search for @BotFather
- Start it using `/start`
- Create a new bot using the `/newbot`command
- Give it a name and a tag (the tag must end with `bot`)
- Now copy the token it gives you

## Requirements
- Pip3
- Python3

## Docker-compose
```yaml
version: '2'
services:
  finderdmibot:
    image: ghcr.io/unict-dmi/finderunictbot
    container_name: finderunictbot
    volumes:
      - <your-settings.yaml>:/app/config/settings.yaml
    restart: unless-stopped
```

### Building locally

```bash
git clone git@github.com:UNICT-DMI/FinderUniCT_Bot.git
cd FinderUniCT_Bot
docker build --tag finderunictbot .
```

---

## Docker CLI
To test the bot with docker compose on Windows follow these steps:
1) Clone the repository
2) Copy the existing `config/settings.yaml.dist` and rename it into `config/settings.yaml`
3) In `token` add your Telegram bot's token
4) Open the terminal on the cloned repository and run ```docker build -t finderunictbot .``` to build the new image
5) Next run ```docker run -v "/c/Users/your/absolute/path/finderunictbot/config/settings.yaml":"/finderunictbot/config/settings.yaml" finderunictbot```

To test it with Linux follow the steps above to the point 4) and:

5) Run ```$ docker run -v "/home/your/absolute/path/finderunictbot/config/settings.yaml":"/finderunictbot/config/settings.yaml" finderunictbot```


## Run live
To test the bot directly on your machine follow these steps:
1) Clone this repository
2) Copy the existing `config/settings.yaml.dist` and rename it into `config/settings.yaml`
3) In `token` add your Telegram bot's token
4) Run `$ python main.py` to start the bot

## Credits