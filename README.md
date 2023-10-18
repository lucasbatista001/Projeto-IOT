
# Projeto IoT com Node-RED

### Instruções:

## Instalação do Node-RED:

Certifique-se de ter o Node-RED instalado em seu ambiente. Se ainda não tiver, siga as instruções de instalação disponíveis [aqui](https://nodered.org/docs/getting-started/installation).

## Importação do Fluxo:

1. Faça o download do arquivo de fluxo disponível neste repositório.

2. Abra o Node-RED.

3. Clique no menu no canto superior direito.

4. Selecione "Import".

5. Cole o conteúdo do arquivo de fluxo e clique em "Import".

## Acesso ao Projeto IoT:

- Acesse a interface interativa do projeto IoT em [https://wokwi.com/projects/377769572783895553](https://wokwi.com/projects/377769572783895553).

   **OU**

  - Se o projeto não estiver mais disponível, utilize o Simulador ESP32 em [https://docs.wokwi.com/pt-BR/guides/esp32](https://docs.wokwi.com/pt-BR/guides/esp32) e o Referência do wokwi-pir-motion-sensor em [https://docs.wokwi.com/pt-BR/parts/wokwi-pir-motion-sensor](https://docs.wokwi.com/pt-BR/parts/wokwi-pir-motion-sensor).

- Configure a conexão conforme mostrado na imagem fornecida.
  
- Baixe e utilize o código em Python disponível no repositório.

  ![pgniot](https://github.com/lucasbatista001/Projeto-IOT/assets/111438250/774296d5-572e-47a4-aaf2-6b187b3e1051)
  
## Conexão dos Fios:

- **Fio Fase (Positivo):** Conecte este fio ao pino 3V3 do módulo ESP. Este pino fornece uma alimentação de 3.3 volts.

- **Fio Neutro (Negativo):** Conecte este fio ao pino GND do módulo ESP. Este pino é o terra, a referência de potencial zero.

- **Saída (Digital):** Conecte este fio ao pino D15 do módulo ESP. Este pino é uma saída digital e será utilizado para enviar sinais ou informações.


## Observações:

1. Certifique-se de configurar corretamente as credenciais e ajustar as configurações no Node-RED.

2. Para informações detalhadas sobre a configuração e personalização, consulte a documentação incluída neste repositório.

3. Simulação deve ser feita no [https://wokwi.com/micropython](https://wokwi.com/micropython).

   
