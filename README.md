# Chatbot de PLN com Rasa

Este projeto é um chatbot desenvolvido com o framework Rasa, focado em Processamento de Linguagem Natural (PLN) em português. O assistente é capaz de:

- Responder saudações e despedidas.
- Informar dados de contato (telefone e e-mail).
- Informar se a empresa está aberta ou fechada, considerando o dia e horário atual ou consultado.

## Estrutura do Projeto

- **actions/**: Scripts de ações customizadas do Rasa, como informar contato e checar horário de funcionamento.
- **data/**: Arquivos de treinamento (NLU, regras, histórias).
- **config.yml**: Configuração do pipeline de NLP e políticas.
- **domain.yml**: Definição de intents, entidades, slots, ações e respostas.

## Como executar

1. Crie e ative o ambiente virtual:
   ```
   python -m venv .env
   .env\Scripts\activate
   ```

2. Instale o Rasa:
   ```
   pip install rasa
   ```

3. Treine o modelo:
   ```
   rasa train
   ```

4. Inicie o shell do assistente:
   ```
   rasa shell
   ```

## Observações

- O pipeline utiliza o modelo SpaCy `pt_core_news_md` e BERT multilíngue.
- Certifique-se de instalar o modelo SpaCy:
  ```
  python -m spacy download pt_core_news_md
  ```

## Licença

Este projeto é acadêmico e para fins educacionais.
