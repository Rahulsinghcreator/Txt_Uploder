import os

API_ID = API_ID = 29540156

API_HASH = os.environ.get("API_HASH", "775d47859519f34f01549344a392280b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6506459683:AAGwGxX8TJSFvuEqOKFWkADbU5k0nzyFyfo")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5943972790))

LOG = -1001802897880

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5943972790").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


