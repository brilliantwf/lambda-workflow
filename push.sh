 git update-index --skip-worktree Kustomize/
 
 git update-index --assume-unchanged Kustomize/base/kustomization.yaml
 git update-index --skip-worktree Kustomize/prod/*

 git pull --rebase origin main
 git push origin main
 git add .
 git commit -m "new commit"
 git push -u origin main
