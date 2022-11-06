# -*_ coding=utf-8 -*-

import json
import random
import sys
import os

class Eattool(object):
    fileexit = os.path.exists('菜单.json')
    warning = "没有找到菜单文件，请将 菜单.json 放到程序同级目录"
    try :
        with open('菜单.json', 'r', encoding='utf8') as fp:
            config = json.load(fp)
            mian = config["mian"]
            mixian = config["mixian"]
            rou = config["rou"]
            shucai = config["shucai"]
            tang = config["tang"]
            out = config["out"]
    except Exception:
        pass


    def __init__(self):
        pass

    def eat_mian(self):
        if self.fileexit == False:
            return self.warning
        else:
            result = random.choice(self.mian)
            return result

    def eat_mixian(self):
        if self.fileexit == False:
            return self.warning
        else:
            result = random.choice(self.mixian)
            return result

    def eat_fan(self):
        if self.fileexit == False:
            return self.warning
        else:
            rou = random.choice(self.rou)
            shucai = random.choice(self.shucai)
            tang = random.choice(self.tang)
            result = rou + '+' + shucai + '+' + tang
            return result

    def eat_out(self):
        if self.fileexit == False:
            return self.warning
        else:
            result = random.choice(self.out)
            return result

