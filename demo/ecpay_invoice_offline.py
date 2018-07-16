#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ecpay_invoice.ecpay_main import *

import time
import random

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'INVOICE'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/Invoice/Issue'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊

# 商品資訊
ecpay_invoice.Send['Items'].append({
    'ItemName': '商品名稱一',
    'ItemCount': 1,
    'ItemWord': '批',
    'ItemPrice': 100,
    'ItemTaxType': 1,
    'ItemAmount': 100,
    'ItemRemark': '商品備註一'
})
ecpay_invoice.Send['Items'].append({
    'ItemName': '商品名稱二',
    'ItemCount': 1,
'ItemWord': '批',
    'ItemPrice': 150,
    'ItemTaxType': 1,
    'ItemAmount': 150,
    'ItemRemark': '商品備註二'
})
ecpay_invoice.Send['Items'].append({
    'ItemName': '商品名稱三',
    'ItemCount': 1,
    'ItemWord': '批',
    'ItemPrice': 250,
    'ItemTaxType': 1,
    'ItemAmount': 250,
    'ItemRemark': '商品備註三'
})

RelateNumber = 'ECPAY' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(
random.randint(1000000000, 2147483647))  # 產生測試用自訂訂單編號
ecpay_invoice.Send['RelateNumber'] = RelateNumber
ecpay_invoice.Send['CustomerID'] = ''
ecpay_invoice.Send['CustomerIdentifier'] = ''
ecpay_invoice.Send['CustomerName'] = 'test'
ecpay_invoice.Send['CustomerAddr'] = 'test'
ecpay_invoice.Send['CustomerPhone'] = ''
ecpay_invoice.Send['CustomerEmail'] = 'test@local.com'
ecpay_invoice.Send['ClearanceMark'] = ''
ecpay_invoice.Send['Print'] = '1'
ecpay_invoice.Send['Donation'] = '0'
ecpay_invoice.Send['LoveCode'] = ''
ecpay_invoice.Send['CarruerType'] = ''
ecpay_invoice.Send['CarruerNum'] = ''
ecpay_invoice.Send['TaxType'] = 1
ecpay_invoice.Send['SalesAmount'] = 500
ecpay_invoice.Send['InvoiceRemark'] = 'SDK TEST Python V1.0.180302'
ecpay_invoice.Send['InvType'] = '07'
ecpay_invoice.Send['vat'] = ''
ecpay_invoice.Send['OnLine'] = False

# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()
print 'RelateNumber：' + str(RelateNumber)
print aReturn_Info

print aReturn_Info['RtnMsg']
print '發票號碼' + aReturn_Info['InvoiceNumber']
assert aReturn_Info['RtnMsg'] == '開立發票成功'