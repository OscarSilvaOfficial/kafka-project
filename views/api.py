from services.kafka import show_topics


# Por padrão as views serão definidas como funções 
# e a unica a ser acessada pela camada de URLs
# e não fazem conversões ou implementações

def topicos():
    return show_topics()