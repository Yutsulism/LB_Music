import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("29735026", ""))
API_HASH = getenv("23cfb762c7b6ae6d64b510e40f4fa3fa", "")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7335225682:AAFsI3jauvK3qY_pVEJ5z35wls8QVLIzROE", None)

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://akhileshsuryavanshi001:AKhilesh001@cluster0.zv0fxgu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002181556863", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6767287493"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("bloodyxmusic01")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-ae7c7519-cd9b-492c-a004-94a2668fdf4a")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Learningbots79/LB_Music", # dont Change this otherwise u get error 🧧
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/yutsulism_x_support_channel")
SUPPORT_CHAT = getenv("SUPPORT_GROUP", "https://t.me/yutsulism_x_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BAHFuHIAPuj6fUdr6vGf7YNiX6PxXc6TLm3iJUjHiG8iyJ8LSA_oI7NEncJOsP7RD50yn-g7_E5mozSmY9e3oKApUrWPdNAxZW6h3Bwcas110AAt7tmMEtTh616u5lu8sRwM_8Hn1bLIolZM6YzLmzZMr0DSO09T4aJNos5YXoDnKwrudrKw0g3Ad1lEVNzR5bO9g9-UvTkrL9SLpXOq2lm3xO1zDgC7Hen7t398WY0tcZP3APO6epqeIbxeV2jEDx6IhPb5n9sY9cwLyZELUsseF3Bso_AuqAiIQSqiDvhB4bFnr0ElWuKAtaHUTPsFTQEoi2xCMCv8roNmIziqU2v0FqwXsQAAAAGTXJzFAA", None)
STRING2 = getenv("BAHFuHIAPuj6fUdr6vGf7YNiX6PxXc6TLm3iJUjHiG8iyJ8LSA_oI7NEncJOsP7RD50yn-g7_E5mozSmY9e3oKApUrWPdNAxZW6h3Bwcas110AAt7tmMEtTh616u5lu8sRwM_8Hn1bLIolZM6YzLmzZMr0DSO09T4aJNos5YXoDnKwrudrKw0g3Ad1lEVNzR5bO9g9-UvTkrL9SLpXOq2lm3xO1zDgC7Hen7t398WY0tcZP3APO6epqeIbxeV2jEDx6IhPb5n9sY9cwLyZELUsseF3Bso_AuqAiIQSqiDvhB4bFnr0ElWuKAtaHUTPsFTQEoi2xCMCv8roNmIziqU2v0FqwXsQAAAAGTXJzFAA", None)
STRING3 = getenv("BAHFuHIAPuj6fUdr6vGf7YNiX6PxXc6TLm3iJUjHiG8iyJ8LSA_oI7NEncJOsP7RD50yn-g7_E5mozSmY9e3oKApUrWPdNAxZW6h3Bwcas110AAt7tmMEtTh616u5lu8sRwM_8Hn1bLIolZM6YzLmzZMr0DSO09T4aJNos5YXoDnKwrudrKw0g3Ad1lEVNzR5bO9g9-UvTkrL9SLpXOq2lm3xO1zDgC7Hen7t398WY0tcZP3APO6epqeIbxeV2jEDx6IhPb5n9sY9cwLyZELUsseF3Bso_AuqAiIQSqiDvhB4bFnr0ElWuKAtaHUTPsFTQEoi2xCMCv8roNmIziqU2v0FqwXsQAAAAGTXJzFAA", None)
STRING4 = getenv("BAHFuHIAPuj6fUdr6vGf7YNiX6PxXc6TLm3iJUjHiG8iyJ8LSA_oI7NEncJOsP7RD50yn-g7_E5mozSmY9e3oKApUrWPdNAxZW6h3Bwcas110AAt7tmMEtTh616u5lu8sRwM_8Hn1bLIolZM6YzLmzZMr0DSO09T4aJNos5YXoDnKwrudrKw0g3Ad1lEVNzR5bO9g9-UvTkrL9SLpXOq2lm3xO1zDgC7Hen7t398WY0tcZP3APO6epqeIbxeV2jEDx6IhPb5n9sY9cwLyZELUsseF3Bso_AuqAiIQSqiDvhB4bFnr0ElWuKAtaHUTPsFTQEoi2xCMCv8roNmIziqU2v0FqwXsQAAAAGTXJzFAA", None)
STRING5 = getenv("BAHFuHIAPuj6fUdr6vGf7YNiX6PxXc6TLm3iJUjHiG8iyJ8LSA_oI7NEncJOsP7RD50yn-g7_E5mozSmY9e3oKApUrWPdNAxZW6h3Bwcas110AAt7tmMEtTh616u5lu8sRwM_8Hn1bLIolZM6YzLmzZMr0DSO09T4aJNos5YXoDnKwrudrKw0g3Ad1lEVNzR5bO9g9-UvTkrL9SLpXOq2lm3xO1zDgC7Hen7t398WY0tcZP3APO6epqeIbxeV2jEDx6IhPb5n9sY9cwLyZELUsseF3Bso_AuqAiIQSqiDvhB4bFnr0ElWuKAtaHUTPsFTQEoi2xCMCv8roNmIziqU2v0FqwXsQAAAAGTXJzFAA", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/9198c701d8d25689e7dee.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/9198c701d8d25689e7dee.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/2167bd450099addae7798.jpg"
STATS_IMG_URL = "https://graph.org/file/2167bd450099addae7798.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/2167bd450099addae7798.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/2167bd450099addae7798.jpg"
STREAM_IMG_URL = "https://graph.org/file/2167bd450099addae7798.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/2167bd450099addae7798.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/2167bd450099addae7798.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/2167bd450099addae7798.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/2167bd450099addae7798.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/2167bd450099addae7798.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
