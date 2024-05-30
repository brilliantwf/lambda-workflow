 git update-index --skip-worktree Kustomize/
 
 git pull --rebase origin main
 git push origin main
 git add python-app/app.py
 git commit -m "new commit"
 git push -u origin main
