# coding: utf-8
__author__ = 'fripSide'

import tensorflow as TF

hello = TF.constant('Hello, TensorFlow')
sess = TF.Session()

print(sess.run(hello))

def generate_domain(year, month, day):
    """Generates a domain name for the given date."""
    domain = ""

    for i in range(16):
        year = ((year ^ 8 * year) >> 11) ^ ((year & 0xFFFFFFF0) << 17)
        month = ((month ^ 4 * month) >> 25) ^ 16 * (month & 0xFFFFFFF8)
        day = ((day ^ (day << 13)) >> 19) ^ ((day & 0xFFFFFFFE) << 12)
        domain += chr(((year ^ month ^ day) % 25) + 97)

    return domain



print(generate_domain(2016, 12, 11))

