As observações não podem ser exportadas de maneira comum, nas importações. Para realizá-las será necessário um caminho um pouco mais complicado por causa do tipo de Autenticação que é necessário para isto. Ela se chama Oauth2 (Online Authentication 2), e demanda de coisas como Segredo do Cliente, Cliente ID e outras coisas.

Estarei realizando a aplicação em um linux

### **1º Passo - Crie uma Aplicação no Hubspot**

- **Crie uma Aplicação no HubSpot:**
    - Vá para [HubSpot Developer Account](https://developers.hubspot.com/).
    - Navegue até "My Apps" e clique em "Create an app".
    - Preencha as informações necessárias, como nome da aplicação, descrição e URLs de redirecionamento (por exemplo, `http://localhost` para testes locais).
    - Em "Auth", selecione "OAuth" e adicione o escopo necessário (como `crm.objects.companies.read` e `crm.objects.companies.write`).
    - De ao seu app um nome que te lembre a Autenticação o Oauth, como Hubspot Oauth. Depois na parte de escopos, você precisará determinar quais escopos você deseja alterar. No caso de você querer importar informações de empresas, é o `crm.company.read`. No caso de criar novos contatos é o `crm.contacts.write`, e caso queira baixar qualquer [*engajement*](https://developers.hubspot.com/docs/api/crm/engagements) de um Deal (negócio) aí é o `crm.deal.read` .
    - Tome cuidado com os escopos, pois você pode fazer muita besteira se colocar escopos mais do que deve.
    - Adicione um link de redirecionamento (por enquanto pode ser um padrão do tipo *https://localhost:3000/oauth-callback*, mas caso você decida seguir a trilha do ngrok, terá de mudá-lo, se for seguir pelo Flask, pode manter esse mesmo. Apenas tome cuidado que no caso de ngrok, ele **precisa** ser http***s***, e não só http
    
- **Obtenha as Credenciais da Aplicação:**
    - Após criar a aplicação, você terá acesso ao `Client ID` e `Client Secret`. Guarde essas informações.

### **3º Passo - Instalar as dependências no terminal**

O terminal é o ambiente que lhe permitirá cuidar desta integração por causa do [localhost](http://localhost) e tudo mais, e o caminho é este (no linux, caso o teu seja Mac ou Wn é só colocar no GPT para ele traduzir para ti): 

1. Abra o terminal (Ctrl + Alt + T)
2. Instale as dependências

Você pode optar pelo Método **Flask** ou pelo Método **Ngrok**

Caso algum processo estiver acontecendo dentro do localhost:3000, é só utilizar o desactive_localhost.bash


### **4º Passo - Obter o token de acesso da Oauth2**

Com o link de redirecionamento ajustado, será necessário manter o Flask ou o Ngrok ativo em uma das abas do terminal. Na outra aba do terminal você deve seguir os passos:

1. **Crie um arquivo Python para o servidor HTTP:**
`oauth_server.py`
	
2. **Executar o Servidor HTTP:**
        
3. **Acessar a URL de Autorização:**
    - Abra um navegador e acesse a URL de instalação de amostra (OAuth), que o próprio aplicativo da Hubspot fornece.
        
4. **Obtenção do TOKEN de acesso:**
    - Nesta nova aba, selecione a sua conta principal do Hubspot (a que deseja importar ou exportar os dados) e siga o processo até que a tela dê em uma pequena linha de código que irá conter os seguintes valores:
    
    - **token_type**: Indica o tipo de token, que no caso é `bearer`, conforme padrão OAuth 2.0.
    - **refresh_token**: Um token utilizado para obter um novo token de acesso quando o atual expira.
    - **access_token**: O token de acesso que você usará para autenticar e acessar recursos protegidos na API do HubSpot. Este token é usado nas requisições HTTP como um cabeçalho `Authorization: Bearer <access_token>`.
    - **expires_in**: O tempo em segundos até o token de acesso expirar. No exemplo, ele expira em 1800 segundos (30 minutos).
    
5. Para testar se deu certo, no Terminal, você pode rodar o comando test_command.bash:
    - Substitua `seu_token_oauth_aqui` pelo seu token OAuth válido.
    - Este comando realiza uma requisição GET para a API de empresas do HubSpot. Ele envia seu token OAuth no cabeçalho `Authorization` com o prefixo `Bearer`.
    - Também é possível testar pelo Postman, mas questione o GPT como fazê-lo que ele lhe orientará.

### **4º Passo - Obter o token de acesso da Oauth2**

Você pode se utilziar de um código em python ou outra linguagem no Databricks, ou pode executar no próprio Terminal:

- Crie um script shell (arquivo.sh) com o comando no Terminal (Substitua ‘arquivo’ pelo nome que deseja):
- E dentro deste arquivo, você adiciona o código da importação ou exportação que deseja fazer. Dentro deste código, provavelmente você precisará o novo Token que conseguiu, ou caso queira deixar automatizado por causa do tempo de expiração, coloque o CLIENT_ID, CLIENT_SECRET e o REFRESH_TOKEN no seu código


### Documentações Adicionais

[Hubspot CRM API Documentation | Associações](https://developers.hubspot.com/docs/api/crm/associations)

[Hubspot CRM API Documentation | Engagements](https://developers.hubspot.com/docs/api/crm/engagements)

[Hubspot CRM API Documentation | Understanding the CRM](https://developers.hubspot.com/docs/api/crm/understanding-the-crm)

[Hubspot CRM API Documentation | Developer Guides Resources](https://developers.hubspot.com/docs/api/developer-guides-resources)

[Hubspot CRM API Documentation | Intro to Auth](https://developers.hubspot.com/docs/api/intro-to-auth)

[Hubspot CRM API Documentation | Usage Details](https://developers.hubspot.com/docs/api/usage-details)

[HubSpot API Reference](https://developers.hubspot.com/docs/api/overview)

[HA | Integrating With HubSpot I: Foundations - A Introducition to Using Oauth With Hubspot](https://app.hubspot.com/academy/19499302/tracks/1092124/1093820/2967?language=en)
