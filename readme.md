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

git config --global user.name "your_github_username"
git config --global user.email "your_github_email"
git config -l
