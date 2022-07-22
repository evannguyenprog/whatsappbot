import os
from whatsapp import WhatsApp

whatsapp = WhatsApp(100, session="mysession")
whatsapp.send_document("Evan", os.path.join(os.getcwd(), "message.txt"))

