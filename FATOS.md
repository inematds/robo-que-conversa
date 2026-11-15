# FATOS — robo-que-conversa (fonte única do guia e do vídeo)

Pesquisa de compra feita em 14/11/2026. **Nada foi comprado nem testado.** Preços mudam todo dia e variam por loja;
no Brasil, somar frete e impostos de importação (Remessa Conforme). "cerca de US$" sempre.

## O que o Nei quer
Um robô (ou aparelho) que **interage com as pessoas**, conversando por voz com uma IA na nuvem (tipo DeepSeek),
e de preferência **anda (rodas)**, tem **sensores, câmera, microfone e voz**, e **Wi-Fi**.

## Como a conversa funciona (vale para todos)
O aparelho não tem a IA dentro. Ele grava a voz → manda pela internet (Wi-Fi) → um servidor transforma em texto,
pergunta à IA (DeepSeek, GPT, Qwen…), transforma a resposta em voz → o aparelho fala e se mexe.
Sem internet ele para de conversar, a menos que a IA rode num computador na mesma rede (ex.: Ollama).

## Grupo A — Robô de mesa (fica parado, mexe a cabeça)
| Produto | Preço | Fonte | Fatos |
|---|---|---|---|
| M5Stack StackChan (kit completo, K151) | cerca de US$ 99 (Switch Science, sem imposto); Pi Hut £ 95 | switch-science.com/products/11129, thepihut.com | Core (ESP32-S3) + Body; 2 servos (360° horizontal, 90° vertical); bateria 550 mAh; firmware de fábrica traz o agente de IA XiaoZhi; app StackChan World escolhe o agente; servidor do projeto é aberto (github.com/m5stack/StackChan). Não confirmei se dá para apontar para DeepSeek próprio. |
| StackChan Core (só a cabeça) | R$ 281,62 no AliExpress (link do Nei, 14/11); cerca de US$ 45 (Switch Science) | AliExpress 1005012587645804; openelab | ESP32-S3 240 MHz, 16 MB flash, 8 MB PSRAM; tela 2,0" 320×240 touch; câmera 0,3 MP (GC0308); sensor de proximidade e luz; IMU 6 eixos + magnetômetro; 2 microfones; alto-falante 1 W; microSD; Wi-Fi 2,4 GHz + BLE |
| StackChan Body (só o corpo) | R$ 344,65 no AliExpress (link do Nei, 14/11) | AliExpress 1005012588163007; docs.m5stack.com StackChan_Body | 2 servos com retorno; bateria 550 mAh; 12 LEDs RGB; infravermelho; touch em 3 zonas; NFC. NÃO funciona sozinho: precisa do Core original (o app não aceita CoreS3 comum). |
| Core + Body comprados separados | R$ 626,27 | soma dos dois links | Comparar com o kit completo antes de comprar. |

## Grupo B — Placas com tela para montar seu assistente (paradas)
| Produto | Preço | Fonte | Fatos |
|---|---|---|---|
| Waveshare ESP32-S3 Touch AMOLED 2,16" | R$ 243,61 no AliExpress (link do Nei, 14/11) | AliExpress 1005012821178507; waveshare.com | Tela AMOLED 2,16" 480×480 touch (a melhor do grupo); ESP32-S3R8, 16 MB flash, 8 MB PSRAM; 2 microfones; IMU 6 eixos; RTC; codec de áudio; Wi-Fi 2,4 GHz + BLE 5; versão com bateria 1000 mAh. Sem câmera. A ficha não confirma alto-falante (tem codec de áudio). |
| Placa ESP32-S3 com LCD 1,54" "IA DeepSeek" (genérica, firmware XiaoZhi) | R$ 118,54 ou R$ 135,71 (2 variantes, link do Nei, 14/11) | AliExpress 1005011874532154; placas parecidas da Spotpear | Tela 240×240; anúncio diz "4 versões". Placa parecida (Spotpear): 2 microfones, microSD, versão touch com IMU. Cerca de US$ 18 nas placas parecidas. |
| Espressif ESP32-S3-BOX-3 (alternativa) | cerca de US$ 45–60 (fontes divergem) | smarthomeexplorer.com | Placa oficial da Espressif; 2 microfones; tela 2,4" touch; alto-falante; palavra de ativação no próprio chip; suporte oficial do Home Assistant; nota 8,4/10 em 3 análises (smarthomeexplorer). Foto oficial: github.com/espressif/esp-box. |

## Grupo C — Robôs com rodas, câmera, microfone e voz (o que o Nei quer)
| Produto | Preço | Fonte | Fatos |
|---|---|---|---|
| SunFounder PiCar-X (versão AI) | **US$ 89,99** na loja oficial (14/11) + Raspberry Pi à parte | sunfounder.com/products/picar-x | Raspberry Pi 5/4/3B+/3B/Zero 2W (Pi NÃO incluso); câmera em 2 eixos; sensor ultrassônico (distância); sensor de linha/escala de cinza; microfone e alto-falante usados nas aulas de voz; LLMs suportados no código: OpenAI, Gemini, Grok, **DeepSeek**, Qwen, Doubao e Ollama (local); voz: Vosk (fala→texto, tem `pt`) e Piper (texto→voz); palavra de ativação configurável. Os exemplos prontos usam GPT-4o-mini e Doubao: DeepSeek = trocar a classe no código (`from picarx.llm import Deepseek`, modelo `deepseek-chat`). Envio da China. Confirmar no anúncio que é a versão AI com microfone. |
| Hiwonder miniAuto Pro (Standard ou Ultimate) | a partir de cerca de US$ 164 (revendedor rcdrone, variantes esgotadas; preço por variante não confirmado) | rcdrone.top/products/miniauto-pro | Placa ESP32 UNO + **módulo WonderLLM** (ESP32-P4 + ESP32-C5): câmera 2 MP 123°, tela 2,0" touch, microfones, alto-falante, palavra de ativação, reconhece voz a até 5 m (1 m com barulho), Wi-Fi 2,4 e 5 GHz; 4 rodas mecanum (anda de lado); ultrassônico RGB; sensor de linha 4 canais; bateria 7,4 V 2000 mAh. Ultimate traz braço com garra. **O Starter NÃO tem câmera, microfone nem alto-falante.** |
| Hiwonder TurboPi Advanced + Raspberry Pi 5 8 GB | **US$ 459,99** na Amazon EUA (atualizado 14/11) | specpicks.com/product/B0FHHPZFVZ | Raspberry Pi 5 incluso; ROS2; câmera HD em 2 eixos; chassi de metal e rodas mecanum (descrição do fabricante); IA multimodal (ChatGPT) com voz; seguidor de linha, reconhecimento de cor e objeto. |
| Hiwonder ROSOrin / JetAuto Pro (nível avançado) | cerca de US$ 374 / US$ 1.500 (só em resultado de busca, não conferido) | busca 14/11 | LiDAR, câmera 3D, ROS2; para quem quer navegação autônoma. Fora do foco. |

## DeepSeek pelo XiaoZhi
Anúncios de kits XiaoZhi (Fruugo, 14/11) dizem que o firmware aceita Qwen2.5, DeepSeek V3, Doubao e Qwen Max. Não testado em nenhum kit.
PiCar-X: bateria = 2 pilhas 18650 (confirmar no anúncio se vêm); Raspberry Pi 5/4/3B+/3B/Zero 2W (Zero 2W só 2,4 GHz).

## Wi-Fi
Todos têm Wi-Fi. ESP32-S3 (StackChan, Waveshare, 1,54", BOX-3): só 2,4 GHz. Raspberry Pi (PiCar-X, TurboPi): 2,4 e 5 GHz.
miniAuto Pro: o módulo WonderLLM tem 2,4 e 5 GHz. Fora de casa: roteador do celular.

## Cuidados
- XiaoZhi (StackChan e placas "DeepSeek"): o servidor público é chinês; a conversa passa por lá. Um fabricante (Spotpear) avisa
  que o reconhecimento pela câmera do servidor XiaoZhi não funciona fora da China.
- Português: XiaoZhi foi feito para chinês; testar reconhecimento e voz em PT. PiCar-X: Vosk tem modelo `pt`.
- DeepSeek cobra por uso (API, barata): a chave é sua, a conta é sua.
- Robô com câmera e microfone perto de criança: ver o projeto irmão robo-ia-crianca.

## Recomendação (por uso)
1. Quer que ande, veja, ouça e fale com DeepSeek, gastando menos: **PiCar-X + Raspberry Pi 5 4 GB** (cerca de US$ 90 + Pi).
2. Quer tudo pronto, com rodas e Pi incluso: **TurboPi** (cerca de US$ 460).
3. Quer simples, com tudo no módulo de IA: **miniAuto Pro Standard** (ver preço da variante).
4. Quer um "bichinho" de mesa com carinha que mexe a cabeça: **StackChan kit completo**.
5. Quer só testar a conversa por voz em PT gastando pouco: **placa de 1,54"** (R$ 118).
