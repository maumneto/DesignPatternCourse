class FrontendCode:
    @staticmethod
    def typescript():
        print('Developing typescript code.')

class BackendCode:
    @staticmethod
    def node():
        print('Developing node code.')

class WebProject:
    def __init__(self):
        self.frontend = FrontendCode()
        self.backend = BackendCode()

    def developApp(self):
        self.frontend.typescript()
        self.backend.node()
        print('Application Developed!')

if __name__ == '__main__':
    webApp = WebProject()
    webApp.developApp()