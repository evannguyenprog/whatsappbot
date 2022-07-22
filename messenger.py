import os
from whatsapp import WhatsApp

from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
print(whatsapp.send_message("Name",":heart: Good!"))  

whatsapp = WhatsApp(100, session="mysession")
whatsapp.send_document("Evan", os.path.join(os.getcwd(), "message.txt"))

