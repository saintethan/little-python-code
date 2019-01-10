'''
Generating two hundred coupons which can be safely sent by Email or used as
parts of urls.
'''

import base64
import os.path

# Construct an object which can generate as many coupons as you want.
class CouponGenerator(object):
    def __init__(self, item_name, item_num):
        self.item_name = item_name # the name of the good
        self.item_num = item_num # the total number of the coupons
        self.raw_code = [] # the set of raw codes
        self.encoded_code = [] # the set of encoded codes

    # The main function
    def coupon_gene(self):
        self.raw_code_gene()
        self.encoded_code_gene()
        self.save_coupon()

    # Generate raw codes, and save them in self.raw_code list.
    def raw_code_gene(self):
        magnitude = len(str(self.item_num))
        for count in range(self.item_num):
            sep_raw_code = ":".join([self.item_name,
                                     self.count_gene(magnitude, count+1)])
            if sep_raw_code not in self.raw_code:
                self.raw_code.append(sep_raw_code)

    # Generalize the form of numbers, i.e. '1' to '001' for a total of 200 numbers.
    def count_gene(self, mag, cou):
        add_num = mag - len(str(cou))
        if add_num == 0:
            return str(cou)
        else:
            add_cou = []
            for count in range(add_num):
                add_cou.append('0')
            add_cou.append(str(cou))
            return "".join(add_cou)

    # Generate encoded codes based on raw codes.
    def encoded_code_gene(self):
        for count in range(len(self.raw_code)):
            encoded_item = base64.urlsafe_b64encode(self.raw_code[count].encode())
            self.encoded_code.append(encoded_item.decode())

    # Save all the encoded codes to a local file.
    def save_coupon(self):
        file_path = os.path.join((os.path.abspath(os.path.dirname(__file__))),
                                 "coupons.txt")
        with open(file_path, "w") as fhand:
            fhand.write("\n".join(self.encoded_code))


if __name__ == "__main__":
    Coupon_gene = CouponGenerator("PDFExpert", 200)
    Coupon_gene.coupon_gene()
