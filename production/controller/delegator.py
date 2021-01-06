class Delegator:
    def __init__(self, delegatee=None, *args, **kwargs):
        self.delegatee = delegatee

    def __getattr__(self, called_method):
        if hasattr(self.delegatee, called_method):
            return getattr(self.delegatee, called_method)
        else:
            return self.dummy

    def dummy(self, *args, **kwargs):
        raise NotImplementedError