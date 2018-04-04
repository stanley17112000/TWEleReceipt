from datetime import datetime, timedelta
import string
import random
def modifyReceiptNum( receipt, delta ):
    receipt_eng = receipt[0:2]
    receipt_num = int(receipt[2:10])
    receipt_num += int(delta)
    return receipt_eng + str(receipt_num)


def modifyDate( date, delta):
    data_list = date.split('/')
    newDate = datetime(int(data_list[0])+1911, int(data_list[1]), int(data_list[2]))
    newDate = newDate + timedelta(days=delta)
    data_list = newDate.strftime("%Y/%m/%d")
    ret = data_list.split('/')
    ret[0] = str (int(ret[0]) - 1911 )
    return '/'.join(ret)

def idGenerator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

