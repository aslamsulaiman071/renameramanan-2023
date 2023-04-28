import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "22980504")

API_HASH = os.environ.get("API_HASH", "b85ecdd508ae39f4e64a08e9a4f9c48d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6167410984:AAEdnIXil9ELF8Uxi53b_i3egnxr0NzpVJk") 

FORCE_SUB = os.environ.get("FORCE_SUB", "sastatony") 

DB_NAME = os.environ.get("DB_NAME","Jatin")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Jatin:Jatin@cluster0.zdkvzab.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/07cfd858071be72375912.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get("ADMIN", "5366891026").split()]

PORT = os.environ.get('PORT', '8080')

WEBHOOK = bool(os.environ.get("WEBHOOK", True))
