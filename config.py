import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "")

API_HASH = os.environ.get("API_HASH", "")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

STRING = os.environ.get("STRING", "")

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5195423974').split()]

PORT = os.environ.get('PORT', '8080')

class temp(object):
    THUMBNAIL = os.environ.get("THUMBNAIL", "AgACAgUAAxkBAAIGRWPuSgboGtGgMHO_IoVg-gtk5I76AAKHszEb-x64Vq2TKplEh60RAAgBAAMCAAN4AAceBA")
