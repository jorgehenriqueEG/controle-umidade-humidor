# controle-umidade-humidor
## Descrição do Problema
Um humidor de tabaco precisa manter a umidade relativa entre 65% e 70%. O sistema deve ler as leituras do sensor e alertar quando o nível sair da faixa ideal.
## Requisitos
- Receber uma lista de leituras de umidade.
- Identificar leituras fora do intervalo [65, 70].
- Calcular a média das leituras válidas.
## Exemplo de Uso
Input: [68, 69, 72, 66, 64]
Saída: Alerta: 2 leituras fora da faixa. Média válida: 67.67%