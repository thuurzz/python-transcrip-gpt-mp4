<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Projeto de transcrição de vídeo do YouTube</title>
</head>
<body>
  <h1>Projeto de transcrição de vídeo do YouTube</h1>
  <p>Este projeto usa a API do YouTube e o PyDub para extrair o áudio de um vídeo do YouTube e criar uma transcrição do áudio.</p>
  <h2>Pré-requisitos</h2>
  <ul>
    <li>Python 3.8 ou superior</li>
    <li>PyTube</li>
    <li>OpenAI</li>
    <li>PyDub</li>
    <li>python-dotenv</li>
  </ul>
  <h2>Instalação</h2>
  <p>Para instalar os pré-requisitos, execute o seguinte comando:</p>
  <pre><code>pip install -r requirements.txt</code></pre>
  <h2>Uso</h2>
  <p>Para usar este projeto, siga estas etapas:</p>
  <ol>
    <li>Execute o arquivo <code>transcript.py</code>.</li>
    <li>Insira o link do vídeo do YouTube.</li>
  </ol>
  <pre><code>python3 transcript.py</code></pre>
  <p>O projeto irá baixar o áudio do vídeo e criar uma transcrição do áudio. A transcrição será salva em um arquivo de texto no diretório <code>transcription</code>.</p>
  <h2>Funcionamento</h2>
  <p>O projeto funciona da seguinte forma:</p>
  <ol>
    <li>O código usa a API do YouTube para baixar o vídeo especificado.</li>
    <li>O código usa o PyDub para extrair o áudio do vídeo.</li>
    <li>O código usa o OpenAI para criar uma transcrição do áudio.</li>
    <li>A transcrição é salva em um arquivo de texto.</li>
  </ol>
  <h2>Melhorias</h2>
  <ul>
    <li>O projeto pode ser melhorado adicionando a capacidade de escolher a qualidade do áudio baixado.</li>
    <li>O projeto pode ser melhorado adicionando a capacidade de escolher o formato do arquivo de áudio baixado.</li>
    <li>O projeto pode ser melhorado adicionando a capacidade de ajustar a duração dos trechos de áudio usados para criar a transcrição.</li>
  </ul>
  <h2>Contribuições</h2>
  <p>Contribuições são bem-vindas. Para contribuir, faça um fork do repositório e envie um pull request com suas alterações.</p>
</body>
</html>
