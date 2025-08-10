# Checklist de Deployment no Render

Use esta checklist para garantir que seu app seja implantado corretamente no Render.

## Antes do Deployment

- [ ] Todos os arquivos Python necessários estão no repositório
- [ ] O arquivo `requirements.txt` contém todas as dependências
- [ ] Os arquivos `setup.sh`, `render_start.sh` e `Procfile` estão configurados
- [ ] O arquivo `.gitignore` está configurado para excluir arquivos sensíveis

## Configuração no Render

- [ ] Criar uma conta no Render (render.com)
- [ ] Conectar ao repositório GitHub
- [ ] Criar um novo Web Service
- [ ] Configurar o ambiente como Python
- [ ] Definir o Build Command como: `pip install -r requirements.txt`
- [ ] Definir o Start Command como: `sh render_start.sh`

## Variáveis de Ambiente

- [ ] Configurar SENDER_EMAIL (para envio de e-mails)
- [ ] Configurar SENDER_PASSWORD (para envio de e-mails)
- [ ] Configurar API_KEY (se necessário)

## Após o Deployment

- [ ] Verificar se o app está online
- [ ] Executar o verificador de deployment (`/check_deployment`)
- [ ] Executar o depurador (`/render_debug`)
- [ ] Verificar logs para erros

## Solução de Problemas Comuns

### Módulos faltando
```
pip install -r requirements.txt
```

### Arquivos não encontrados
Verifique se todos os arquivos Python estão no repositório e se os caminhos estão corretos.

### Problemas de permissão
```bash
chmod -R 777 .
```

### Variáveis de ambiente não configuradas
Configure no painel do Render > Environment.

## Como Testar o Deployment

1. Acesse a URL fornecida pelo Render
2. Adicione `/check_deployment` à URL para executar o verificador
3. Adicione `/render_debug` à URL para executar o depurador
4. Verifique os logs no painel do Render