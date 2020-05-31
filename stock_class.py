class Stock:
    def __init__(self):
        self.__name = ''
        self.__stock_price = 0
        self.__total_stock = 0
        self.__total_dept = 0
        self.__total_subtraction = 0
        self.__ev = 0
        self.__eidta = 0
        self.__stock_value = 0

    # getting name
    def get_name(self):
        return self.__name

    # setting name
    def set_name(self, new_name):
        self.__name = new_name
        print('name had changed')

    