import smtplib

DEFAULT_EMAIL = "fredalocampo@gmail.com"


def send_email(destination, msg, email_addr=DEFAULT_EMAIL, subject="Daily Quote"):
    """

    :param subject: email subject
    :param email_addr: Source of email address
    :param destination: Deliver to destination
    :param msg: Email Content
    :return:
    """
    try:
        with open('../resources/google_pw.txt') as pw:
            user_password = pw.read()
    except FileNotFoundError:
        google_pw = ''
        print('Constants file not found, please provide a file or hardcode the Google app password ')
    else:
        # Enter your Google APP password
        google_pw = f'{user_password}'

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email_addr, password=google_pw)
            connection.sendmail(from_addr=email_addr, to_addrs=destination,
                                msg=f'''Subject: {subject}\n\n{msg} ''')

    except smtplib.SMTPException as error:
        print(f'Could not send email due to {error}')
    else:
        print(f'Email sent to {destination}')


