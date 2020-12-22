from jinja2 import Environment, FileSystemLoader

def escrever_arquivo_resultado(nome_arquivo, resultado):
    with open(nome_arquivo, 'w') as arquivo_html:
        template = _carregar_template()
        conteudo = _renderizar_resultado(template, resultado)
        _escrever_arquivo(arquivo_html, conteudo)

def _carregar_template():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    return env.get_template('resultado.html')

def _renderizar_resultado(template, resultado):
    return template.render(resultado=resultado)

def _escrever_arquivo(arquivo, conteudo):
    arquivo.write(conteudo)
