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