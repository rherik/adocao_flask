## Projeto desenvolvido com o framework Flask para incentivo à adoção de vira-latas.

![site_adocao_viralatas](static/imgs/img_site.png)


### Tecnologias utilizadas:
- Flask
- Docker
- Gunicorn
- ElephantSQL
- AWS s3 Bucket
- Bootstrap5

### Tarefas:
  &#9744; Implementar cadastro e login de usuários

  &#9744; Remover bootstrap e transferir histórias para a página inicial

  &#9745; Atualizar função de update para atualizar imagem e url de instagram

  &#9745; Padding-botton minima do footer

  &#9745; Adicionar opção de cadastrar imagem no banco de dados

  &#9745; Consertar navbar
    
  &#9745; Fazer deploy

### Como rodar(Ubuntu):

1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. flask run

Ou

4. ./docker_entrypoint.sh


### Como rodar(Docker):

1. docker build -t nome_da_imagem .
2. docker run -ip 5000:5000 nome_da_imagem



### Erro atual:
- Não remove imagem do bucket aws ao deletar post em produção
- Padding da página deletar
