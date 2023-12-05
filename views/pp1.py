# -- coding: utf-8 --
# date：2023/12/4 11:03
# author: ZhangXu

from flask import blueprints

pp1 = blueprints('pp1', __name__)


@pp1.route("/f1")
def f1():
    return 'f1'


@pp1.route("/f2")
def f2():
    return 'f2'
