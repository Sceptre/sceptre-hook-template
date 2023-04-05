# -*- coding: utf-8 -*-

from sceptre.hooks import Hook


class Custom(Hook):
    def run(self):
        """
        run is the method called by Sceptre. It should carry out the work
        intended by this hook.
        """
        print(self.argument)
