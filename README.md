# CatchTawawa

<h3><img  src="https://img.shields.io/github/license/EKOISMYLOVE/CatchTawawa"/></h3>

## Introduction

This project uses twitter API to catch @Strangestone tweet (Tawawa on monday) and then uses telegram bot to send message of tweet for user or group.

Uses cron to schedule for building on Github Actions.

## Setup

1. Create a telegram bot. [How to Create telegram bot.](https://core.telegram.org/bots#6-botfather)
2. Get bot id and user id(chat id). [StackOverflow - Telegram Bot - how to get a group chat id?](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)
3. Create a twitter developer project and get bearer_token. [Twitter developer Documentation](https://developer.twitter.com/en/docs/platform-overview)
4. Clone this project.
5. Set three environment secrets. Please check secrets name and .github/workflows/main.yml parameters, make sure they are same. [Using environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)
* **TELEGRAM_TO** : Your telegram userId or chatId.
* **TELEGRAM_TOKEN** : Your telegram bot token.
* **TWITTER_BEARER_TOKEN** : Your twitter bearer_token.
6. Set Github Action and edit .github/workflows/main.yml to test. (cron parameter or option of "on")
7. (optional) If you want to catch other twitter users' tweet, just edit parameter ```sample_rules``` and set condition.

## Package
These packages I use, **THANKS!!**

* [MDSK-UltraIN/TawawaBot_forTelegram](https://github.com/MDSK-UltraIN/TawawaBot_forTelegram)
* [twitterdev/Twitter-API-v2-sample-code](https://github.com/twitterdev/Twitter-API-v2-sample-code)
* [theskumar/python-dotenv](https://github.com/theskumar/python-dotenv)
* [appleboy/telegram-action](https://github.com/appleboy/telegram-action)