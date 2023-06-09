Detecção de Linguagem de Sinais usando Distâncias de Referência - Python
-
- Neste projeto, o objetivo principal é criar um modelo que identifique as letras do alfabeto em língua de sinais, excluindo as letras que requerem movimentos específicos para serem identificadas.

- Irá utilizar como dados as coordendas das landmarks da mão encontrada via webcam, tendo como referências os seguintes pontos:
<img width="1073" alt="hand-landmarks" src="https://github.com/joaoangnes/Sign-Language-Detection-using-Landmarks-Python/assets/74597614/b57347b6-7a5a-4132-bba2-7761222d9182">

- Mas para esse projeto, eu considerei apenas as distancias dos pontos das pontas dos dedos e o começo da mão, conforme as linhas em roxo do exemplo a seguir:

![exemple-distances-land-mark](https://github.com/joaoangnes/Sign-Language-Detection-using-Distances-Python/assets/74597614/b922d1c5-758f-4a35-9992-21336b977558)

## Estrutura dos Arquivos

O repositório contém vários arquivos para treinamento do modelo de detecção. Aqui está um resumo das funcionalidades de cada arquivo:

HandTrackingModule.py

    - Este arquivo armazena todas as funções importantes para identificar os pontos de referência das mãos e parametrizar as bibliotecas utilizadas.
    - Serve como arquivo base para todo o projeto.

CollectImages.py

    - Este arquivo cria as imagens que serão utilizadas no treinamento.
    - Segue as instruções passo a passo exibidas na webcam.
    - Captura 150 fotos com a mão direita e 150 fotos com a mão esquerda. (Todos os parâmetros podem ser facilmente modificados)

CreateDataSet.py

    - Este arquivo recupera todas as imagens coletadas e armazena os pontos de referência dos 20 pontos identificados pela biblioteca mediapipe em um arquivo 'pickle'.

main.ipynb

    - Este notebook Jupyter recebe os dados coletados, processa-os e treina um modelo para identificação.
    - Normalização dos dados: ✅
    - Balanceamento dos dados: ✅
    - Ajuste de hiperparâmetros: Utilizando o método RandomizedSearchCV
    - Modelo de Treinamento: RandomForestClassifier
    - Modelo de Validação: Cross Validate

    Após todas as validações, o modelo é salvo usando o pickle com o nome 'model.p'.

## Bibliotecas Utilizadas

- cv2
- HandTrackingModule
- Pickle
- Os

## Demonstração

Modelo em funcionamento:

Mão Direita:

<img src="https://github.com/joaoangnes/Sign-Language-Detection-using-Distances-Python/assets/74597614/3beab86a-c345-44bd-ab63-0dd5746e920c" width="160">

Mão Esquerda:

<img src="https://github.com/joaoangnes/Sign-Language-Detection-using-Distances-Python/assets/74597614/c5031f71-09d8-4e3b-a78d-2ae60028f6d0" width="160">

## Lições Aprendidas

Foi uma ótima experiência de aprendizado explorar a ciência de dados e concluir este projeto.
Enfrentei muitas dificuldades no início para entender como cada biblioteca funcionava e confesso que ainda tenho muitas dúvidas, especialmente em relação ao desempenho da detecção dos pontos de referência usando a biblioteca mediapipe.

Em resumo, este projeto proporcionou valiosas oportunidades de aprendizado e, apesar de alguns contratempos, consegui criar um modelo que identifica todas as letras estáticas do alfabeto da língua de sinais.

Também criei outro repositório que segue a mesma estrutura, mas utiliza as distâncias principais dos pontos de referência das mãos como dados de entrada e inferência. 

Aqui está o link para o repositório: https://github.com/joaoangnes/Sign-Language-Detection-using-Landmarks-Python


## Referências

https://www.youtube.com/watch?v=wa2ARoUUdU8&t=12s&ab_channel=Murtaza%27sWorkshop-RoboticsandAI
https://www.youtube.com/watch?v=pDXdlXlaCco&ab_channel=NicholasRenotte
https://www.youtube.com/watch?v=MJCSjXepaAM&t=2947s&ab_channel=Computervisionengineer