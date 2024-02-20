from datetime import datetime as dt
from random import randint
from send_emails_gmail.birthday_wisher.utils.email_sender import send_email
from send_emails_gmail.birthday_wisher.utils.read_file import CustomFileReader

today = (dt.now().month, dt.now().day)
reader = CustomFileReader('../resources/birthdays.csv')

# 1. Update the birthdays.csv
birthday_dict = reader.load_birthday_dict()

# 2. Check if today matches a birthday in the birthdays.csv
if today in birthday_dict:
    birthday_person = birthday_dict[today]["name"]
    print(f'Happy Birthday {birthday_person}')
    letter_path = f'../resources/letter_templates/letter_{randint(1, 3)}.txt'
    random_letter = str(CustomFileReader(letter_path, header=False))
    # Add Signature and Name
    formatted_letter = (
        random_letter.replace('[SIGNATURE]', 'Jannick')
        .replace('[NAME]', birthday_person)
    )

    print(formatted_letter)
    send_email(destination="sample+email+happy@gmail.com", msg=formatted_letter, subject="Happy Birthday")

