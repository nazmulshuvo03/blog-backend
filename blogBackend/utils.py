from __future__ import division
from rest_framework.renderers import JSONRenderer
from django.http.response import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.core.validators import validate_email
from datetime import datetime, date
import time
import re
import random


def generate_user_id():
    user_id = "".join(
        [random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVXYZ') for i in range(10)])
    return user_id


def generate_user_name(first="", last=""):
    digits = "".join(
        [random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVXYZ') for i in range(10)])
    if first and last:
        return first + "_" + last + "_" + digits
    else:
        return digits


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def group_list(user):
    groups = [item.name for item in user.groups.all()]
    return groups


def primary_group(user):
    if user:
        groups = [item.name for item in user.groups.all()]
        if not groups:
            return 'GUEST'
        return groups[0]
    return 'GUEST'


def validate_pan_number(value):
    """
    Validates if the given value is a valid PAN number or not, if not raise ValidationError
    """
    if re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', value):
        return True
    else:
        return False


# Print any message
def xprint(agument1, argument2=None,
           argument3=None, argument4=None,
           argument5=None, argument6=None,
           argument7=None, argument8=None,
           argument9=None, argument10=None,
           argument11=None, argument12=None,
           argument13=None, argument14=None,
           argument15=None, argument16=None,
           argument17=None, argument18=None,
           argument19=None, argument20=None,
           argument21=None, argument22=None,
           argument23=None, argument24=None,
           argument25=None, argument26=None):
    print("*************************************************************")
    print_value = str(agument1)
    if argument2:
        print_value += ', ' + str(argument2)
    if argument3:
        print_value += ', ' + str(argument3)
    if argument4:
        print_value += ', ' + str(argument4)
    if argument5:
        print_value += ', ' + str(argument5)

    if argument6:
        print_value += ', ' + str(argument6)

    if argument7:
        print_value += ', ' + str(argument7)

    if argument8:
        print_value += ', ' + str(argument8)

    if argument9:
        print_value += ', ' + str(argument9)

    if argument10:
        print_value += ', ' + str(argument10)

    if argument11:
        print_value += ', ' + str(argument11)

    if argument12:
        print_value += ', ' + str(argument12)

    if argument13:
        print_value += ', ' + str(argument13)

    if argument14:
        print_value += ', ' + str(argument14)

    if argument15:
        print_value += ', ' + str(argument15)

    if argument16:
        print_value += ', ' + str(argument16)

    if argument17:
        print_value += ', ' + str(argument17)

    if argument18:
        print_value += ', ' + str(argument18)

    if argument19:
        print_value += ', ' + str(argument19)

    if argument20:
        print_value += ', ' + str(argument20)

    if argument21:
        print_value += ', ' + str(argument21)

    if argument22:
        print_value += ', ' + str(argument22)

    if argument23:
        print_value += ', ' + str(argument23)

    if argument24:
        print_value += ', ' + str(argument24)

    if argument25:
        print_value += ', ' + str(argument25)

    if argument26:
        print_value += ', ' + str(argument26)

    #     if argument27:
    #         print_value += ', ' + str(argument27)
    #

    print(print_value)
    print("*************************************************************")


def is_string_email(email):
    try:
        valid_email = validate_email(email)
        if valid_email:
            return True
        else:
            return False
    except:
        return False


def is_string_phone_number(phone_number):
    try:
        if phone_number.isdigit() and len(phone_number) == 10:
            return True
        return False
    except:
        return False


def is_string_pan_number(pan_number):
    try:
        if len(pan_number) == 10:
            if pan_number[0:5].isalpha() and pan_number[5:9].isdigit() and pan_number[-1].isalpha():
                return True
        return False
    except:
        return False


def is_string_aadhar_number(aadhar_number):
    try:
        if aadhar_number.isdigit() and len(aadhar_number) == 12:
            return True
        return False
    except:
        return False


def convert_string_to_float(value):
    try:
        value = float(value.replace(",", "").replace("'", ""))
    except:
        raise ValueError('failed to convert ' + str(value) + ' to float')

    return value


def get_age(dob):
    if not dob:
        return ''
    age = date.today().year - dob.year
    return age


def roundup_100(x):
    return x if x % 100 == 0 else x + 100 - x % 100


def roundup_1000(x):
    return round(x / 1000) * 1000


def convert_two_decimal_float(number=0.00, type=None):
    number = float("{00:.2f}".format(number))
    if type == "string":
        number_array = str(number).split('.')
        float_part = number_array[1]
        if len(float_part) == 1:
            number = str(number_array[0] + "." + float_part + "0")
    return number


def return_boolean(value, condition):
    try:
        if value == condition:
            return True
        return False
    except:
        return False


def get_file_name_time_stamp():
    return datetime.now().strftime('_%d%m%Y_%H%M')


def merge_dictionaries(*dictionaries):
    result = {}
    for dictionary in dictionaries:
        result.update(dictionary)
    return result


def create_datetime_id():
    return datetime.now().strftime('%y%m%d%H%M%S')


def create_date_id():
    return datetime.now().strftime('%y%m%d')


def create_time_id():
    return int(time.time() * 100000)


def create_16_bit_uid():
    date_id = create_date_id()[5:15]
    time_id = create_time_id()
    return str(date_id) + str(time_id)


def search_in_workbook(sheet, key):
    try:
        for row in range(sheet.nrows):
            for column in range(sheet.ncols):
                if key in sheet.cell(row, column).value:
                    return [row, column]
    except:
        pass
    return None


def primary_group(user):
    groups = [item.name for item in user.groups.all()]
    if not groups:
        return 'GUEST'
    return groups[0]


def generate_id_from_datetimenow():
    id = str(datetime.now()).replace('-', '').replace(':',
                                                      '').replace('.', '').replace(' ', '')
    return id


def ordinal_indicator(number):
    numeric_value = str(number)
    last_digit = numeric_value[-1]
    if last_digit == '1':
        return numeric_value + 'st'

    elif last_digit == '2':
        return numeric_value + 'nd'

    elif last_digit == '3':
        return numeric_value + 'rd'
    else:
        return numeric_value + 'th'


def date_ordinal(day):
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    return suffix


def unique_list(unsorted_list):
    # order preserving
    checked = []
    for e in unsorted_list:
        if e not in checked:
            checked.append(e)
    return checked


def get_single_key_from_value(dictionary, search_value):
    for key, value in dictionary.items():
        if type(value) is dict:
            found_string = get_key_from_value(value, search_value)
            if found_string:
                return found_string
        elif value == search_value:
            return key
    return None


def none_to_zero(num):
    if num:
        return num
    else:
        return 0


def get_gst_breakup(amount):
    base_charge = float(amount / float(0.18 + 1))
    goods_and_services_tax = convert_two_decimal_float(amount - base_charge)
    return base_charge, goods_and_services_tax


def get_pvot_charges(amount):
    base_charge = float(amount / float(0.30 + 1))
    pvot_charges = convert_two_decimal_float(amount - base_charge)
    return base_charge, pvot_charges
