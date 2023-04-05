# -*- coding: utf-8 -*-

from hook.custom import Custom


class TestCustom:
    hook = Custom()

    def setup(self):
        self.hook.argument = "test"

    def test_custom(self):
        self.hook.run()
