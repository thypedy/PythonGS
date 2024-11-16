# README - Calculadora de Energia Renovável a partir de Biomassa

## Pesquisa Bibliográfica
- [Energia dos resíduos](https://web.bndes.gov.br/bib/jspui/bitstream/1408/2523/1/A%20BS%2033%20Perspectivas%20do%20setor%20de%20biomassa%20de%20madeira%20para%20a%20geração%20de%20energia_P.pdf)
  
- [Formula do calculo](https://www3.epa.gov/ttn/atw/utility/fnl_biomass_cogen_TSD_04_19_07.pdf)

## Descrição do Projeto
Este projeto é uma **calculadora de energia renovável** que permite calcular a quantidade de energia gerada a partir de diferentes tipos de biomassa. Utiliza dados de poder calorífico inferior (PCI) para diferentes tipos de biomassa e um valor de eficiência fixa de 30%. A aplicação fornece funcionalidades para:
- Inserir diferentes tipos de biomassa e suas quantidades.
- Calcular a energia gerada em kWh.
- Exibir as energias geradas por tipo de biomassa e a porcentagem de cada tipo no total.
- Salvar e carregar os dados de biomassa para um arquivo de texto.

O objetivo do projeto é fornecer uma interface simples e interativa para os usuários que desejam entender a viabilidade energética de diferentes biomassa como fontes renováveis.

## Funcionalidades
- **Escolher o tipo de biomassa**: O usuário pode selecionar entre quatro tipos de biomassa (resíduos agrícolas, resíduos de madeira, resíduos alimentares e estrume animal).
- **Inserir a quantidade de biomassa**: Após selecionar o tipo de biomassa, o usuário insere a quantidade em quilogramas (kg).
- **Calcular a energia gerada**: Com base na quantidade de biomassa inserida e no PCI de cada tipo, o sistema calcula a energia gerada em kWh.
- **Exibição de energia total**: A energia total gerada por todos os tipos de biomassa é exibida.
- **Armazenamento de dados**: O usuário pode salvar as quantidades de biomassa inseridas e carregar os dados de um arquivo salvo anteriormente.
- **Interface gráfica simples**: A interface é construída utilizando a biblioteca `Tkinter`, proporcionando uma interação intuitiva e fácil.

## Instruções de Uso
1. **Escolher o Tipo de Biomassa**:
   - Utilize o menu suspenso para escolher o tipo de biomassa (1 - Resíduos Agrícolas, 2 - Resíduos de Madeira, 3 - Resíduos Alimentares, 4 - Estrume Animal).
   
2. **Inserir a Quantidade**:
   - Digite a quantidade de biomassa em quilogramas (kg) no campo de entrada de quantidade.

3. **Adicionar Biomassa**:
   - Clique no botão "Adicionar Biomassa" para registrar o tipo e a quantidade de biomassa. O cálculo da energia será feito automaticamente e exibido na lista de energia.

4. **Salvar Dados**:
   - Clique em "Salvar Dados" para armazenar a biomassa e suas quantidades em um arquivo de texto chamado `dados_biomassa.txt`.

5. **Carregar Dados**:
   - Clique em "Carregar Dados" para ler os dados salvos anteriormente e exibi-los na interface.

6. **Encerrar o Programa**:
   - Clique em "Encerrar" para fechar o aplicativo.

## Requisitos
- Python 3.11 ou superior
- Bibliotecas padrão do Python: `tkinter`, `messagebox`
- Não é preciso instalar nenhuma biblioteca a cima

## Dependências
- Não há dependências externas para este projeto, além das bibliotecas padrão do Python.

## Como Rodar o Projeto
1. Certifique-se de que o Python 3.x esteja instalado em seu sistema.
2. Baixe ou clone o repositório deste projeto.
3. Abra o terminal ou prompt de comando na pasta onde o arquivo Python está localizado.
4. Execute o código com o comando:
   ```bash
   python PythonGS.py
## Detalhes Técnicos

### Cálculo da Energia

A energia gerada é calculada utilizando a seguinte fórmula:

\[
\text{Energia} = \frac{\text{PCI} \times \text{Eficiência} \times \text{Quantidade}}{\text{Conversão MJ/kWh}}
\]

Onde:

- **PCI**: Poder Calorífico Inferior (MJ/kg) para o tipo de biomassa selecionado.
- **Eficiência**: A eficiência é fixada em **30%** para o cálculo da energia.
- **Conversão MJ/kWh**: A conversão de **MJ para kWh** é feita utilizando o fator de conversão **3.6**.
