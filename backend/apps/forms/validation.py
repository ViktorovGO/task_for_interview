from datetime import datetime
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from email_validate import validate as m_valid


def validation(field, field_type, out_type=False):
    def_type = 'text'
    if is_valid_date(field):
        def_type = 'date'
    elif is_valid_phone(field):
        def_type = 'phone'
    elif is_valid_email(field):
        def_type = 'email'

    return def_type == field_type if not out_type else def_type


def is_valid_date(value):
    
    try:
        datetime.strptime(value, '%Y-%m-%d')
    except ValueError:
        try:
            datetime.strptime(value, '%d.%m.%Y')
        except:
            return False
    return True


def is_valid_phone(value):
    return carrier._is_mobile(number_type(phonenumbers.parse(value, region='RU'))) if value.isdigit() else False
    


def is_valid_email(value):
    
    return m_valid(email_address=value,
    check_format=True,
    check_blacklist=False,
    check_dns=False,
    check_smtp=False,
    smtp_debug=False)


