#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ecpay_invoice.ecpay_main import *

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'CHECK_MOBILE_BARCODE'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/Query/CheckMobileBarCode'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['BarCode'] = '/RXNOFER'

# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()
print aReturn_Info
print aReturn_Info['RtnMsg']
