class Frontend:
    def devCode(self):
        self._typescript()

    @staticmethod
    def _typescript():
        print('Developing typescript code.')

class Backend:
    def devCode(self):
        self._node()

    @staticmethod
    def _node():
        print('Developing node code.')

class Coder:
    def __init__(self):
        self.frontend = Frontend()
        self.backend = Backend()

    def devCode(self):
        self.frontend.devCode()
        self.backend.devCode()

class WebApplication:
    def __init__(self):
        self._coder = Coder()

    def devCode(self):
        print('Application Developed!')
        return self._coder.devCode()

if __name__ == '__main__':
    webApp = WebApplication()
    webApp.devCode()