ECPAY電子發票Python模組
=======================

綠界電子發票建置中...

安裝
-----


利用pip

.. code-block:: python

    pip install ecpay_invoice

匯入模組

.. code-block:: python

    from ecpay_invoice.ecpay_main import *

其他範例請看demo

change log:

2018-08-09 修正lovecode判定，移除raise錯誤，只印出錯誤訊息供參考

2018-08-06 更新CustomerIdentifier錯誤判斷

2018-08-02 更新錯誤提示方式

2018-07-30 更新錯誤判斷式

2018-07-19 更新demo範例註解

2018-07-17 更新商品單價可以為小數，諾驗證沒有通過會停止程式

