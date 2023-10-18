# Importando as bibliotecas necessárias
import network                               # Biblioteca para operações de rede
import time                                  # Biblioteca para operações com tempo
from machine import Pin                      # Módulo para interagir com os pinos do hardware
from umqtt.simple import MQTTClient          # Módulo para comunicação MQTT (umqtt)

# Parâmetros do Servidor MQTT
MQTT_CLIENT_ID = "micropython-motion-demo"   # Identificador único do cliente MQTT
MQTT_BROKER    = "broker.mqttdashboard.com"  # Endereço do servidor MQTT
MQTT_USER      = "projetoIOT"                # Nome de usuário para autenticação no servidor MQTT
MQTT_PASSWORD  = "87532543"                  # Senha para autenticação no servidor MQTT
MQTT_TOPIC     = "wokwi-motion"              # Tópico MQTT onde as mensagens serão publicadas

# Configurando o pino para o sensor PIR
sensor_pir = Pin(15, Pin.IN)                # Configurando o pino 15 como entrada para o sensor PIR

# Conectando-se à rede Wi-Fi
print("Conectando ao WiFi", end="")
sta_if = network.WLAN(network.STA_IF)       # Obtendo uma interface de rede sem fio
sta_if.active(True)                         # Ativando a interface
sta_if.connect('Wokwi-GUEST', '')           # Conectando à rede Wi-Fi (SSID: 'Wokwi-GUEST')
while not sta_if.isconnected():             # Aguardando até que a conexão seja estabelecida
    print(".", end="")
    time.sleep(0.1)
print(" Conectado!")

# Conectando-se ao servidor MQTT
print("Conectando ao servidor MQTT... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.connect()                            # Estabelecendo a conexão com o servidor MQTT
print("Conectado!")

# Loop principal para detecção de movimento
while True:
    motion_detected = sensor_pir.value()    # Verificando o valor do sensor PIR

    if motion_detected:
        message = "Motion Detected"
        print("Reporting to MQTT topic {}: {}".format(MQTT_TOPIC, message))
        client.publish(MQTT_TOPIC, message)  # Publicando a mensagem no tópico MQTT

    time.sleep(3)                            # Aguarda 3 segundo antes de verificar novamente

#by Lucas Batista 