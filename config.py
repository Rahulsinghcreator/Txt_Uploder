import os

API_ID = API_ID = 

API_HASH = os.environ.get("API_HASH", "465cca6fa782695983d49db306e0f8be")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6443500984:AAFnlR6aZGhP1v_GJpAyUQViwdrrq385h98")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 585731991))

LOG = -1001952769436

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "585731991").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


