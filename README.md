# geradorQRCode
Simples gerador de QRCode utilizando o módulo pyqrcode para python.
Para saber mais acesse https://nsworld.com.br/como-gerar-facilmente-qrcode-com-python/

<!-- wp:tadv/classic-paragraph -->
<h3>Criando um script simples</h3>
<p>Agora que já instalamos o pyqrcode vamos por a mão na massa:</p>
<h4>Declarando a codificação</h4>
<p>Quando você inseri algum caractere acentuado no seu script, por exemplo “á”, um aviso é mostrado na execução:</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted"><em>sys:1: DeprecationWarning: Non-ASCII character ‘\xe1’ in file foo.py on line 3, but no encoding declared;</em></pre>
<!-- /wp:preformatted -->

<!-- wp:tadv/classic-paragraph -->
<p><span>A codificação ASCII é o padrão para códigos fonte, então é preciso avisar o Python que seus fontes usam outra. Para o português é ISO-8859-1, ou seu similar mais curto latin-1. Basta colocar um comentário especial na primeira ou segunda linha do código.</span></p>
<p>Sistemas e editores atuais vêm configurados com a codificação UTF-8, que abrange a maioria dos idiomas existentes. Se este for seu caso, use:</p>
<pre># coding: utf-8</pre>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:tadv/classic-paragraph -->
<p>Neste caso utilizaremos o enconding UTF-8 para nosso script:</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>#!/usr/bin/env python
# -*- coding: utf-8 -*-</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":3} -->
<h3>Importar Módulos</h3>
<!-- /wp:heading -->

<!-- wp:tadv/classic-paragraph -->
<p>Importaremos o módulo pyqrcode e a partir dele importaremos a função qrcode:</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>#Importar módulo pyqrcode 
import pyqrcode
#Importar QRCode do módulo pyqrcode
from pyqrcode import QRCode</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":3} -->
<h3>Entrada e Saída</h3>
<!-- /wp:heading -->

<!-- wp:tadv/classic-paragraph -->
<p>Para nosso script iremos inserir uma entrada para que o usuário digite a URL que desejar e depois solicitaremos a ele um nome de saída para salvar o QRCode. </p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>#String que será representada pelo QRCode
s = raw_input("Digite a url a ser transformada: ")
#Nome parao arquivo de saida 
n = raw_input("Digite o nome de saida: ")</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2>Gerar o QRCode</h2>
<!-- /wp:heading -->

<!-- wp:tadv/classic-paragraph -->
<p>Para gerar o QRCode utilizaremos a função <strong>create </strong>e passaremos como parâmetro a string de entrada<strong> s</strong>.</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>#Gerar o QRCode
url = pyqrcode.create(s)</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2>Gerando Saída</h2>
<!-- /wp:heading -->

<!-- wp:tadv/classic-paragraph -->
<p>Para gerar e salvar a saída utilizaremos a função <strong>sgv</strong> concatenada com a string de entrada <strong>n</strong>, mais a escala(<strong>scale</strong>) que gostaríamos de utilizar para nosso QRCode.</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>#Criar e salvar o arquivo com o nome inserido
url.svg( n +".svg", scale = 8)</code></pre>
<!-- /wp:code -->

