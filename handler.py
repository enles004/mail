from jinja2 import FileSystemLoader, Environment, select_autoescape

import config
from mail import MailSender

smtp_config = {"smtp_server": config.smtp_server,
               "smtp_port": config.smtp_port,
               "username": config.sender_email,
               "password": config.pass_email,
               "sender_email": config.sender_email}


class MailEnv:

    def set_env_mail(self, templates: str, filename: str, **kwargs):
        env = Environment(loader=FileSystemLoader(templates),
                          autoescape=select_autoescape())
        template = env.get_template(filename)
        body = template.render(kwargs)
        return body


def send_mail_de():
    subject = "Diem De"
    templates = "mail_templates"
    filename = "mail_content.html"
    data = {"username": "Dê"}
    body = MailEnv().set_env_mail(templates=templates, filename=filename, **data)
    MailSender(**smtp_config).send_mail(body=body, subject=subject, email_to="duongduong05031999@gmail.com")


send_mail_de()
