print("Please enter the following information:")

print()

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
email_add = input('Enter yout email address? ')
phone_no = input('Enter your phone number? ')
job_title = input('Enter your job title? ')
id_number = input('Enter your id number? ')
hair_color = input('Enter your hair color? ')
eye_color = input('Enter your eye color? ')
month = input('Enter your month? ')
training = input('Currently training? Yes or No? ')

info = f"""The ID Card is:
----------------------------------------
{last_name.upper()}, {first_name.capitalize()}
{job_title.title()}
ID: {id_number}

{email_add.lower()}
{phone_no}

Hair: {hair_color.capitalize():15} Eyes: {eye_color.capitalize()}
Month: {month.capitalize():14} Training: {training.capitalize()}
----------------------------------------"""


print(info)