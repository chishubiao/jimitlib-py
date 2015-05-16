#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/5/16'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

from jimit import Commons

router_table = {}


class Router():

    def __init__(self):
        pass

    @staticmethod
    def not_found():
        return Commons.exchange_state(50100)

    @staticmethod
    def launcher(**kwargs):
        action = kwargs.get('action', None)
        launcher = router_table.get(action, Router.not_found)
        print launcher()
