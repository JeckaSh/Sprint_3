import datetime


class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {
            "чипсы": 50,
            "кола": 100,
            "печенье": 45,
            "молоко": 55,
            "кефир": 70,
        }
        self.__tax_rate = {
            "чипсы": 20,
            "кола": 20,
            "печенье": 20,
            "молоко": 10,
            "кефир": 10,
        }

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError(
                "Нельзя добавить товар, если в его названии нет символов или их больше 40"
            )
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items +=1

    def delete_item_from_check(self, name):
        if name not in self.name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -=1

    def check_amount(self):
        total = []
        total_price = 0

        for item in self.name_items:
            total.append(self.__item_price[item])
        
        for e in total:
            total_price += e
        
        if len(total) > 10:
            total_price = total_price - ((total_price / 100) * 10)
            print(total_price)
        else:
            print(total_price)

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        nds = 0

        for i in self.name_items:
            if self.__tax_rate[i] == 20:
                twenty_percent_tax.append(i)
                total.append(self.__item_price[i])

        for j in total:
            nds += j * 0.2

        if len(total) > 10:
            nds = nds - ((nds / 100) * 10)
            return nds
        else:
            return nds

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        nds = 0

        for i in self.name_items:
            if self.__tax_rate[i] == 10:
                ten_percent_tax.append(i)
                total.append(self.__item_price[i])

        for j in total:
            nds += j * 0.1

        if len(total) > 10:
            nds = nds - ((nds / 100) * 10)
            return nds
        else:
            return nds

    def total_tax(self):
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()