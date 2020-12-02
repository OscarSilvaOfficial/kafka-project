import kafka
from services.convert import set_to_json

# Na camada de services pode se feito a conversão de dados
# e se necessário a implementação de classes, porém nunca
# deve ser acessado diretamente pela camada de urls


def show_topics():
    consumer = kafka.KafkaConsumer()
    topicos = set_to_json(consumer.topics())
    return topicos
    
def create_topic(topic, value):
    producer = kafka.KafkaProducer(bootstrap_servers='localhost:9092')

    try:
        producer.send('topico1', b'topico')
    except Exception as e:
        print(e)
        return 'Erro na criação do tópico'

    return 'Tópico criado' 