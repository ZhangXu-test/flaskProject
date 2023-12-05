# -- coding: utf-8 --
# date：2023/12/4 11:04
# author: ZhangXu
from flask import blueprints

pp2 = blueprints('pp2', __name__)


@pp2.route("/f3")
def f3():
    return 'f3'


@pp2.route("/f4")
def f4():
    return 'f4'
