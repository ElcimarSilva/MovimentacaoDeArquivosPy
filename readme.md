novo teste git

Estas são as mensagens iniciais do git

echo "# projetogit" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ElcimarSilva/projetogit.git
git push -u origin main


git remote add origin https://github.com/ElcimarSilva/projetogit.git  #serve para direcionar o local para o remeto
git branch -M main #serve para renomear a branch, no caso para main, o padrão é master
git push -u origin main #serve para empurrar de fato as alterações realizadas, no caso precisa revisar se é a main ou master


Para o problema do autenticação do token
https://stackoverflow.com/questions/68775869/support-for-password-authentication-was-removed-please-use-a-personal-access-to

git config --global user.name "your_github_username"  serve para definir um username default na maquina
git config --global user.email "your_github_email" serve para definir um email default na maquina
git config -l 

mais comandos git
git checkout -b  serve para criação de um branch
git checkout serve para alternar entre branches

git status ver o status da branch

git push origin nomedabranch serve para subir os arquivos, quando se esta na main não é preciso do origin porém quando se esta em outra branch é necessario especificar qual é ela.

No ambiente profissional utilizado para trabalhar, usamos chave ssh que foi confugurado através deste link 
https://support.atlassian.com/bitbucket-cloud/docs/set-up-an-ssh-key/

Video explicação git 
https://www.youtube.com/watch?v=UBAX-13g8OM
tempo 27:00