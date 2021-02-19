class PlaceOrders
    def __init__(self, num_retries=3, typeOfDelay="10", interface):
        self.num_retries = num_retries
        self.typeOfDelay = typeOfDelay

    def place(object):
        try:
            order = Orders.publish(object2)

        if type(order=="Exception"):


        except:
            order = retry(object2, num_retries, typeOfDelay)
            if order == None:

        return order        
        
    def retry(object, num_retries, typeOfDelay):
        order = Orders.publish(object2)
        while not order and num_retries>=1:
            wait(typeOfDelay)
            try:
                order = Orders.publish(object2)
            except:
                pass
            num_retries-=1
        return order




