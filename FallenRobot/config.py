class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "7686800"
    API_HASH = "3a55030126000c9b78fe046bbc36c1ad"

    CASH_API_KEY = "AEKON8UIK9U7Q30J"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://njzozbxl:dHdhVBweev-2Iq389fuWCvseIQXK5wm9@bubble.db.elephantsql.com/njzozbxl"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001361069722)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://3bd6e165809be4:O2bMUfNYcawIR1Gq@cluster0.k4ty0gf.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://graph.org/file/d395af77536d353c436fb.jpg"

    SUPPORT_CHAT = "ndbotsupport"  # Your Telegram support group chat username where your users will go and bother you

    UPDATE_CHANNEL = "ndpowerlogs"  # Your Telegram support CHANNEL username where your users will go and bother you

    TOKEN = "6706039742:AAEpivSIUBLTxzw1xI7S69Pdk4MTQycy__E"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "C9AMYFRW2D83"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5115485603  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
