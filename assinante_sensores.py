import paho.mqtt.client as mqtt
import json

broker = "10.110.18.11"
port = 1883

topic_temp = "sensor/temperatura" #sensor01
topic_umid_ar = "sensor/umidade_ar" #sensor02
topic_umid_solo = "sensor/umidade_solo" #sensor03
topic_pressao = "sensor/pressao" #sensor04
topic_co2 = "sensor/co2" #sensor05

def on_message(client, userdata, msg):
    mensagem = msg.payload.decode()

    dados = json.loads(mensagem)

    print("======================= DADOS RECEBIDOS =============================")

    print("-------------------Temperatura---------------------")
    print(f"Sensor: {dados[0]['sensor']}")
    print(f"Temperatura: {dados[0]['temperatura']} {dados[0]['unidade']}")
    print(f"Timestamp: {dados[0]['timestamp']}")
    print("----------------------------\n")

    print("-------------------Umidade do ar---------------------")
    print(f"Sensor: {dados[1]['sensor']}")
    print(f"Umidade do ar: {dados[1]['umidade_ar']} {dados[1]['unidade']}")
    print(f"Timestamp: {dados[1]['timestamp']}")
    print("----------------------------\n")

    print("-------------------Umidade do solo---------------------")
    print(f"Sensor: {dados[2]['sensor']}")
    print(f"Umidade do solo: {dados[2]['umidade_solo']} {dados[2]['unidade']}")
    print(f"Timestamp: {dados[2]['timestamp']}")
    print("----------------------------\n")

    print("-------------------Pressão---------------------")
    print(f"Sensor: {dados[3]['sensor']}")
    print(f"Pressão: {dados[3]['pressao']} {dados[3]['unidade']}")
    print(f"Timestamp: {dados[3]['timestamp']}")
    print("----------------------------\n")

    print("-------------------CO2---------------------")
    print(f"Sensor: {dados[4]['sensor']}")
    print(f"CO2: {dados[4]['co2']} {dados[4]['unidade']}")
    print(f"Timestamp: {dados[4]['timestamp']}")
    print("----------------------------\n")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect(broker, port, 60)

client.subscribe(topic_temp)
client.subscribe(topic_umid_ar)
client.subscribe(topic_umid_solo)
client.subscribe(topic_pressao)
client.subscribe(topic_co2)

client.on_message = on_message

client.loop_forever()