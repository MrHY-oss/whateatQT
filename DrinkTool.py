# -*- coding=utf-8 -*-
import configparser
import random


class DrinkTool(object):
    config = configparser.ConfigParser()
    filepath = r'config.ini'
    config.read(filepath, encoding='utf-8')

    def __init__(self):
        pass

    def henaicha(self):
        try:
            naicha = self.config['drink']['naicha']
        except Exception:
            naicha = "配置文件错误，请检查config.ini填写是否正确"
        list = naicha.split("|")
        result = random.choice(list)
        return result

    def heguocha(self):
        try:
            guocha = self.config['drink']['guocha']
        except Exception:
            guocha = "配置文件错误，请检查config.ini填写是否正确"
        list = guocha.split("|")
        result = random.choice(list)
        return result

    def hecaffee(self):
        try:
            caffee = self.config['drink']['caffee']
        except Exception:
            caffee = "配置文件错误，请检查config.ini填写是否正确"
        list = caffee.split("|")
        result = random.choice(list)
        return result




if __name__ == "__main__":
    a = DrinkTool()
    b = a.henaicha()
    print(b)
    c = a.heguocha()
    print(c)

