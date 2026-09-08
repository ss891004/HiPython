# HiPython


修改提交缓存大小为500M，或者更大的数字
git config --global http.postBuffer 524288000

先删除要删除的远程仓库名：git remote rm [远程仓库名] 
然后再新增远程仓库：git remote add [远程仓库名] [新的仓库地址]

例如：
git remote rm origin 
git remote add origin https://github.com/vuejs/vue.git

