import os
from twilio.rest import Client

sid = os.environ.get("TWILIO_SID")
token = os.environ.get("TWILIO_TOKEN")
numero = os.environ.get("TWILIO_PHONE")

cliente = Client(sid, token)
mensaje = cliente.messages.create(
    body="Hola mundo!",
    from_=numero,
    to="+59897313415"
)
