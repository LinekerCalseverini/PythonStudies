# Enviando E-mails SMTP com Python
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template

from dotenv import load_dotenv  # type: ignore

load_dotenv()


# Caminho arquivo HTML
CAMINHO_HTML = Path(__file__).parent / 'aula185.html'

# Dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# Configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = remetente
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de Texto
with open(CAMINHO_HTML, 'r') as f:
    texto_arquivo = f.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Helena')

# Transformar nossa mensagem em MIMEMultiPart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso!')
