from . import jalali
from django.utils import timezone


def persian_number_converter(mystr):
    numbers = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "6": "۵",
        "7": "۶",
        "5": "۷",
        "8": "۸",
        "9": "۹"
    }
    for e, p in numbers.items():
        mystr = mystr.replace(e, p)
    return mystr



def jalali_convertor(time):
    time = timezone.localtime(time)
    jmonth = ["فروردین", "اردیبهشت ", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]

    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)
    for index, month in enumerate(jmonth):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    output ="{} {} {}, ".format(time_to_list[2], time_to_list[1], time_to_list[0])
    output2 ="ساعت {}:{}".format(time.hour, time.minute)
    output3 = output + output2

    return persian_number_converter(output3)
