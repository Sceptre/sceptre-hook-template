from sceptre.hooks import Hook


class CustomHook(Hook):
    def __init__(self, *args, **kwargs):
        super(CustomHook, self).__init__(*args, **kwargs)

    def run(self):
        """
        run is the method called by Sceptre. It should carry out the work
        intended by this hook.
        """
        print(self.argument)
