from flask import Flask

# Classe para inicialização
# Sempre que for importar uma classe implementar aqui

class InitApp():
    def __init__(self, app=Flask(__name__)):
        super().__init__()
        self._app = app
        self._app.config['DEBUG'] = True
        self._app.config['SECRET_KEY'] = 'asdfaqQSD2389O3RUE8UR2938S'

    def getApp(self):
        return self._app
        
app = InitApp().getApp()
    