from utils.write_log import writeExceptionToFile

def formatPrice(price=""):
    """ Format display price
        Example:
            price = "1" -> 1.00
            price = "1.5" -> 1.50
            price = "1.55" -> 1.55
    """
    try:
        price = str(price)
        if price != "" and price != None:
            if "." in price:
                if len(price) == price.index(".") + 2:
                    price += "0"
                else:
                    pass
            else:
                price += ".00"
        else:
            price = ""
        return price
    except Exception as e:
        writeExceptionToFile()
        return ""