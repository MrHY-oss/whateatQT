1、UI转PY的命令：pyuic5 -o WhatEatQT.py WhatEatQT.ui

{
  "mian": ["鸡杂面","肥肠面"],
  "mixian": ["牛肉米线","郡花米线"],
  "rou": ["猪肝","肉丝"],
  "shucai": ["白菜","豌豆尖"],
  "tang": ["豆腐汤","鸡蛋汤"]
}


2、打包（去命令行模式）
pyinstaller -F -w .\WhatEat.py
