from flask import Flask, request 
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client 

app = Flask(__name__)


account_sid = 'TU_ACCOUNT_SID'
auth_token = 'TU_AUTH_TOKEN'
twilio_num = 'whatsapp: +numero de telefono'

client= Client(account_sid, auth_token)

def send_initial_message(to):
    client.messge.create(
        body="Hola! Bienvenido al Contacto de AMPAC, inicia con un 'hola' para obtener información.",
        from_=twilio_num,
        to=to
    )

@app.route("/bot", methods=['POST'])
def bot():
    incoming_msg=request.values.get('Body','').lower()
    sender=request.values.get('From')
    if 'start' in incoming_msg or 'hola' in incoming_msg:
        send_initial_message(sender)
    resp= MessagingResponse()
    msg= resp.message()
    if 'hola' in incoming_msg:
        response = "Hola!, 'informacion'"
    elif 'adios' in incoming_msg:
        response = "Adios!, Que tengas un buen dia."
    else: 
        response = 'Lo siento, no entiendo, di hola para informacion '
    msg.body(response)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)