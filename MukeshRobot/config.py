
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "11107466" # integer value, dont use ""
    API_HASH = "303837af39dfd53ff9b60a56f6ca3bc6"
    TOKEN = "6071310208:AAENJ2u7EgsU0Akn2q7xaAeH4gN4z198F_8"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5977523092 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "new_devil_world"  # Your own group for support, do not add the @
    START_IMG = "https://graph.org/file/0405a54a58733cbb572cc.jpg"    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://devilop:devilop123@devilserver.bhep18a.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = "f44f5f1e-8d2e-4638-b79b-5ca0282ad934"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "9UJJJV11OMHIJRZ6"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "XSJUR9B0XIMH"
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    CHATBOT_API="" # get it from @FallenChat_Bot using /token
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
