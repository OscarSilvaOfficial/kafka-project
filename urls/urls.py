from configurations.config import app
from views.api import topicos

# Deve apenas definir as rotas

app.add_url_rule('/topicos', 'topicos', topicos, methods=['GET'])
