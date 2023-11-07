<h2>Projeto para aprendizado do framework Flask para desenvolver um blog de adoção de vira-latas.</h2>

<p>
  <img src="static/imgs/img_site.png" width="850" alt="site_adocao_viralatas">
</p>
<h3>Imagens obtidas do pinterest</h3>

<h3>Documentação das tecnologias utilizadas</h3>

<h3>Tarefas:</h3>
<ol>
    <li>Refatorar css e scss</li>
    <li>Consertar navbar</li>
    <li>Adicionar opção de cadastrar imagem no banco de dados</li>
    <li>Fazer deploy</li>
</ol>

<h3>Como rodar(Ubuntu):</h3>
<ol>
    <li>python3 -m venv venv</li>
    <li>source venv/bin/activate</li>
    <li>pip install -r requirements.txt</li>
    <li>flask run</li>
</ol>

<h3>Como rodar(Docker):</h3>
<ol>
    <li>docker build -t ~nome_da_imagem~ .</li>
    <li>docker run -ip 5000:5000 ~nome_da_imagem~</li>
</ol>


<h2>Erro atual:</h2>
<p>Consertar erro ao deletar um post ele continua a ser listado(Forçar recarregamento da página)</p>
<p>sqlalchemy.orm.exc.UnmappedInstanceError: Class 'builtins.NoneType' is not mapped</p>
<p></p>
