import paho.mqtt.client as mqtt
import time
import random
import json

broker = "10.110.18.11"
port = 1883

topic_temp = "sensor/temperatura" #sensor01
topic_umid_ar = "sensor/umidade_ar" #sensor02
topic_umid_solo = "sensor/umidade_solo" #sensor03
topic_pressao = "sensor/pressao" #sensor04
topic_co2 = "sensor/co2" #sensor05

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect(broker, port, 60)

while True:
    dados = [
        {
            "sensor": "sensor01",
            "temperatura": round(random.uniform(20, 30), 2),
            "unidade": "C",
            "timestamp": time.time()
        },
        {
            "sensor": "sensor02",
            "umidade_ar": round(random.uniform(70, 97)),
            "unidade": "%",
            "timestamp": time.time()
        },
        {
            "sensor": "sensor03",
            "umidade_solo": round(random.uniform(60, 80)),
            "unidade": "%",
            "timestamp": time.time()
        },
        {
            "sensor": "sensor04",
            "pressao": round(random.uniform(130, 220), 1),
            "unidade": "Pa",
            "timestamp": time.time()
        },
        {
            "sensor": "sensor04",
            "co2": round(random.uniform(400, 600)),
            "unidade": "ppm",
            "timestamp": time.time()
        }
    ]

    mensagem = json.dumps(dados)

    client.publish(topic_temp, mensagem)
    client.publish(topic_umid_ar, mensagem)
    client.publish(topic_umid_solo, mensagem)
    client.publish(topic_pressao, mensagem)
    client.publish(topic_co2, mensagem)

    print(f"Enviado: {mensagem}")

    time.sleep(10)