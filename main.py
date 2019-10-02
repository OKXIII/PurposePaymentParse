# import re
#
# def GetPaymentInfo():
#     resultfile=open(r'D:\Projects\PycharmProjects\PurposePaymentParse\paymentresult.csv',"w")
#     for fileline in open("D:\Projects\PycharmProjects\PurposePaymentParse\payment.csv", encoding="utf-8"):
#         line=fileline.rstrip('\n').strip()
#         linesep=line.strip(';')
#         print (linesep)
#     resultfile.write("The End")
#     resultfile.close()
#     return 0

import csv
import re

base =["счет", "счету","договор", "договору"]

with open(r'D:\Projects\PycharmProjects\PurposePaymentParse\payment.csv', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=';', doublequote=True, quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if len(row[3])>0:
            result = re.findall(r"(счет)|(договор)", row[3].lower())
            if len(result)>0:
                result = re.findall(r"(((счет)|(договор))у?\s{0,3}№?.*(б/н)?от\s{0,5}(\d{2}\.\d{2}\.\d{2,4}))", row[3].lower())
                print (row[3])
                print(result)


# def hello():
#     GetPaymentInfo()
#     print("End of Parse")
#
# hello()