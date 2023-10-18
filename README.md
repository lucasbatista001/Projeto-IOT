
# Bem-vindo ao Projeto IoT com Node-RED e ESP32!

Este repositório é dedicado à apresentação e execução de um projeto inovador de Internet das Coisas, desenvolvido utilizando as ferramentas Node-RED e ESP32.

## Objetivo do Projeto:

Nosso principal objetivo é criar uma solução eficiente de IoT para a contagem de pessoas, utilizando o microcontrolador ESP32. A integração do Node-RED e do sensor de movimento não apenas coleta dados, mas também proporciona uma visualização gráfica. Estamos comprometidos em oferecer uma experiência integrada e acessível no vasto campo da Internet das Coisas.

## Como Navegar por Este Repositório:

- Consulte o README para obter instruções detalhadas sobre a configuração e execução do projeto.

- Explore o código-fonte para compreender a implementação e personalização possíveis.

- Fique à vontade para contribuir, fornecer feedback ou tirar dúvidas através das issues.

## Observações Importantes:

Este código está disponível para uso e modificação. Caso faça alterações, certifique-se de documentar as mudanças no README e seguir as diretrizes da licença.

Agradecemos por explorar o Projeto IoT! Divirta-se experimentando e contribuindo para a evolução deste projeto.

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

   
