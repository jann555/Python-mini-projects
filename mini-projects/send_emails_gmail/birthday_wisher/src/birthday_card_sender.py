from datetime import datetime

from send_emails_gmail.birthday_wisher.utils.email_sender import send_email
from send_emails_gmail.birthday_wisher.utils.read_file import CustomFileReader
reader = CustomFileReader('../resources/birthdays.csv')
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
