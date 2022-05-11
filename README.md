# for routine_code
path_change.py

# Install
git clone git@github.com:lishh75/routine_code.git

cd routine_code

pip install . --use-feature=in-tree-build

or for a specific path (e.g. nbodykit-env):

pip install . --use-feature=in-tree-build --target=/home/lishaohong/anaconda3/envs/nbodykit-env/lib/python3.8/site-packages/

or for update:

pip install . --use-feature=in-tree-build --target=/home/lishaohong/anaconda3/envs/nbodykit-env/lib/python3.8/site-packages/ --upgrade


# Git configure
git config --global user.name "lishh75"

git config --global user.email "1625848901@qq.com"

# create remote repositories (in github)

## for a new machine in local
ssh-keygen -t rsa -C "1625848901@qq.com"  

cd .ssh

cat id_rsa.pub

## copy it in "SSH Keys" of setting of github

## git clone new repositories


# git common code 
git status

git add xxx file (for modified file) 

git commit -m "xx" (submit modified information)

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



