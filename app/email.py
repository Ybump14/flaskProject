from threading import Thread

from flask import render_template
from flask_mail import Message

from app import mail
from . import main


def send_email(to, subject, template, **kwargs):
    msg = Message(main.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=main.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[main, msg])
    thr.start()
    return thr


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
