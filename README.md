<h2> Projeto de Análise de Dados </h2>

<p> Este é o meu primeiro projeto pessoal, o desenvolvi com o intuito de praticar meus conhecimentos em Python e em análise de dados com pandas. Projetei este script para filtrar um dataframe, que contém informações das temperaturas históricas de uma cidade de um determindado país. </p>

<h2> Sobre Este Código</h2>

<p> O código realiza o tratamento de tabelas com valores vazios, retirando-os juntamente com algumas colunas que não foram necessárias para o projeto, em seguida renomeia cada coluna para legibilidade em português, logo após é definida uma função na qual filtra o período de data e cidade especificados como entrada, tratando possíveis entradas inválidas ou cidades que não estão inclusas neste dataframe e por fim, exibe a temperatura média da cidade dentro do período informado. </p>

<h2> Arquivo Utilizado </h2>

<p> Você pode baixar o arquivo neste link: https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data?resource=download </p>

<h2> Observações </h2>

<p> Pelo fato de ser um arquivo disponibilizado na web para fins didáticos, o mesmo possui algumas limitações, como por exemplo a data máxima que é "01/09/2013", você pode conferir isso utilizando "print(dataset['Data'].max())", caso não queira que um erro seja exibido. </p>
