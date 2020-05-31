class Stock:
    def __init__(self):
        self.__name = ''
        self.__stock_price = 0
        self.__total_stock = 0
        self.__total_dept = 0
        self.__total_subtraction = 0
        self.__ev = 0
        self.__ebidta = 0
        self.__stock_value = 0

    # getting name
    def get_name(self):
        return self.__name

    # setting name
    def set_name(self, new_name):
        self.__name = new_name
        print('name had changed')

    # setting stock price
    def set_stock_price(self, stock_price):
        self.__stock_price = stock_price

    # getting stock price
    def get_stock_price(self):
        return self.__stock_price

    # setting total number of stock
    def set_total_stock(self, total_stock):
        self.__total_stock = total_stock

    # getting total number of stock
    def get_total_stock(self):
        return self.__total_stock

    # setting total dept
    def set_total_dept(self, total_dept):
        self.__total_dept = total_dept

    # getting total dept
    def get_total_dept(self):
        return self.__total_dept
