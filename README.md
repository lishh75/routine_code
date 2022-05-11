# Git configure
git config --global user.name "lishh75"

git config --global user.email "1625848901@qq.com"

# create remote repositories (in github)

## for a new machine in local
ssh-keygen -t rsa -C "mojf3@mail2.sysu.edn.cn"  

cd .ssh

cat id_rsa.pub

## copy it in "SSH Keys" of setting of github

## git clone new repositories


# git common code 
git status

git add 

git commit -m "xx"

git push

## version control
git log

git reflog

git reset --hard commit_id

eg: git reset --hard HEAD^

git checkout -- file

git reset HEAD file

## https://www.liaoxuefeng.com/wiki/896043488029600 help for using git


# for routine_code
path_change.py

# Install
git clone git@github.com:lishh75/routine_code.git

cd routine_code

pip install . --use-feature=in-tree-build

or for a specific path (e.g. nbodykit-env)

pip install . --use-feature=in-tree-build --target=/home/lishaohong/anaconda3/envs/nbodykit-env/lib/python3.8/site-packages/



