# tmdbwrapper/tv.py

class TV(object):
    def __init__(self, id):
        self.id = id
        return

    def info(self):
        return {'id': self.id}
