import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "27709822"))
    API_HASH = os.environ.get("API_HASH", "a30de8d316e15153c76c64342b86546b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5555669937:AAGFc2aiVS378Y0vbccPGHC0b2cddcAroyI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQArft7txkSP_TQvb1oD3j5XQm_rt1IcD7J2KFfgwkDe1ZssQ0hyHgO3OHwE16uL01NOPy45aZefeny7Svaw31Nxi_plBHljOPibXniHKt7r1ZUNV0-9ZJpu96CG418VpO9VxGd3LL6WK8pvUx0HpPBele9vLUYrAbjl14hRKdHv-lv-exEntlCget19LTBGfxlU-aeOBU38vqxKN4aJhFI9CavxJcyd6sEl0lCcTGqxqHiE-PmbNhIV4pkrcsyS-IGUYAxp2f-3U7L4hTq0-TH7vSKPpKHBrrDmD5giveXdRZhH_Xxg9jcsx2IzLoVun5QEdt5YC5TN_Q_7JztQf4DcAAAAAUalmTAA")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("we4peoplebot")
    SUPPORT = os.environ.get("SUPPORT", "chafoot) # Your Support
    CHANNEL = os.environ.get("CHANNEL", "we4people") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
