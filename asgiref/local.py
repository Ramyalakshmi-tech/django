import threading


class Local(threading.local):
    def __init__(self, *args, **kwargs):
        super().__init__()
