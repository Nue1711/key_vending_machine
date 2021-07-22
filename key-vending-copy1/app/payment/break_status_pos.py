#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# -*- coding: utf-8 -*-
# ====================================================
# Created By : Trung Duc Nguyen
# Created Date : 
# ====================================================

def breakStatus(status=""):
    """ Translate code to text format status

        Attribute:
            status: code format
        
        Return: text format            
    """
    __switcher = {
        "0015":"Incorrect PIN",
        "0034":"No network connection detected",
        "1003":"Transaction Interrupt, Card remove from the reader",
        "1004":"Transaction Interrupt, Cancelled by the payer",
        "1012":"Terminal error",
        "1102":"PreAuth ID not found",
        "1010":"Zero Amount",
        "0025":"Terminal busy"
    }
    return __switcher.get(status,"Invalid status")