import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z]{1}'*[a-z]*\s?[A-Z]{1}[a-z]*-*[A-Z]*[a-z]*"
name_regex = re.compile(name)

phone_number = r"\(?[0-9]{3}[\)\s|-]*[0-9]{3}-?[0-9]{4}"
phone_regex = re.compile(phone_number)

email_address = r"[a-z]*\.?[a-z|0-9]*@[a-z]*\.com"
email_regex = re.compile(email_address)
