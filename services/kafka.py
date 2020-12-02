import kafka
from services.convert import set_to_json

# Na camada de services pode se feito a conversão de dados
# e se necessário a implementação de classes, porém nunca
# deve ser acessado diretamente pela camada de urls


def show_topics():
    consumer = kafka.KafkaConsumer()
    topicos = set_to_json(consumer.topics())
    return topicos
    
def create_topic(topic):
    producer = kafka.KafkaProducer(bootstrap_servers='localhost:9092')

    try:
        producer.send('str(topic)', b'kafka')
        print(topic)
    except Exception as e:
        raise e
    return 'Tópico criado' 