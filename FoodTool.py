# -*- coding=utf-8 -*-
import configparser
import random


class FoodTool(object):
    config = configparser.ConfigParser()
    filepath = r'config.ini'
    config.read(filepath, encoding='utf-8')

    def __init__(self):
        pass

    def chimian(self):
        try:
            mian = self.config['food']['mian']
        except Exception:
            mian = "配置文件错误，请检查config.ini填写是否正确"
        list = mian.split("|")
        result = random.choice(list)
        return result

    def chimixian(self):
        try:
            mixian = self.config['food']['mixian']
        except Exception:
            mixian = "配置文件错误，请检查config.ini填写是否正确"
        list = mixian.split("|")
        result = random.choice(list)
        return result

    def waimianchi(self):
        try:
            out = self.config['food']['out']
        except Exception:
            out = "配置文件错误，请检查config.ini填写是否正确"
        list = out.split("|")
        result = random.choice(list)
        return result

    def chifan(self):
        try:
            rou = self.config['food']['rou']
            sucai = self.config['food']['sucai']
            tang = self.config['food']['tang']
        except Exception:
            errinfo = "配置文件错误，请检查config.ini填写是否正确"
            return errinfo
        rou_list = rou.split("|")
        sucai_list = sucai.split("|")
        tang_list = tang.split("|")
        rou_result = random.choice(rou_list)
        sucai_result = random.choice(sucai_list)
        tang_result = random.choice(tang_list)
        result = rou_result+"+"+sucai_result+"+"+tang_result
        return result



if __name__ == "__main__":
    a = FoodTool()
    b = a.chimian()
    print(b)
    c = a.chimixian()
    print(c)
    d = a.chifan()
    print(d)
    e = a.waimianchi()
    print(e)
