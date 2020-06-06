class Stock:
    def __init__(self):
        # done 종목명
        self.__name = ''
        # done 주가
        self.__stock_price = 0
        # done 전체 주
        self.__total_stock = 0
        # done 시가총액
        self.__market_cap = 0
        # done 총 부채
        self.__total_dept = 0
        # done 시가 총액과 총부채를 더한 값에서 빼야하는 금액
        self.__total_subtraction = 0
        # done Enterprise Value 기업 가치
        self.__ev = 0
        # done 감각상각비, 세금 등을 더한 값  EBIDTA
        self.__ebidta = 0
        # done 기업가치
        self.__corporate_value = 0

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

    # adding total dept
    def add_total_dept(self, extra_dept):
        self.__total_dept += extra_dept

    # adding total subtraction
    def add_total_subtraction(self, extra_subtraction):
        self.__total_subtraction += extra_subtraction

    # setting market cap
    def calc_market_cap(self):
        self.__market_cap = self.__stock_price * self.__total_stock

    # setting Enterprise Value
    def calc_enterprise_value(self):
        self.__ev = (self.__market_cap + self.__total_dept) - self.__total_subtraction
