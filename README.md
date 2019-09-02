# sysLog
Sistema de login
Primeiro programa de login de usuário
Implementações:
-Verificação se o arquivo que salva os dados de Usuário e senha existe, se não cria-lo.
-Input do usuário para 'cadastro', 'login' ou sair do programa.
  -Cadastro
    -Informar nome de usuário.
      -Verificar se o nome informado já existe no sistema.
      -Informa Senha do Usuário.
        -Verifica se a senha tem mais de 8 caracteres.
        -salva a senha e hash "md5".
    -Salva os dados informados no arquivo.
  -Login
    -Informa nome de um usuário cadastrado.
      -Verifica se o usuário existe
      -Informa senha referente a este usuário
        -Valida se a senha informada está correta
          -Informa status do login
