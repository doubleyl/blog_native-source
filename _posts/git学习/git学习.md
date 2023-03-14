---
title: git学习
date: 2023-03-10 01:56:04
categories: 
  - git学习
---



收藏夹里的小程序





#### ~git rebase换基

当前分支branch 从根到最新提交为 A->B->C->D

从A的另一个分支有新的提交

A->E->F

在当前分支用 git rebase anotherBranch

则复制BCD 删除branch，再以anotherBranch最新提交为根创建分支

最后:

branch: A->E->F->B->C->D

anotherBranch:A->E->F(即不会影响anotherBranch)



#### ~git cherry-pick c1 c2 c3 c4

将任意其他分支的提交c1 c2 c3 c4复制到当前分支



#### ~git merge anotherBranch

**仍是不影anotherBranch,其最新提交位置不变**

只是在branch分支上调整，将anotherBranch上的提交与branch上最新的提交合并，产生一个新的提交加到branch上

#### ~git commit --amend

这次提交当作对最新提交的修改，只会使最新提交C2变为C2' 而不会产生新的提交

可以通过git rebase -i HEAD~num 来调整分支，将要修改的C2调整到末端，修改后再用一次调整到适当位置

或 使用cherry-pick 先复制一个C2修改后再将其他的复制过来

#### ~标签tag

作为**锚点**

git tag tagName c1(提交名,没有则为HEAD)

用于某个重要提交，这个提交较为稳定，一般不变

**git describe <ref>** 

产生输出，描述离你最近的锚点 ref为能被git识别成提交记录的引用，不指定则为HEAD

<tag>_ <numCommits>_ g<hash>

tag 表示的是离 ref 最近的标签， numCommits是表示这个 ref与 tag相差有多少个提交记录， hash表示的是你所给定的 ref 所表示的提交记录哈希值的前几位。



#### ~删除提交 git reset --hard HEAD

将返回到上次提交的状态

--mixed 默认

移动HEAD指针，改变暂存区，不变工作区

--soft 回退到某个版本

仅移动HEAD指针，不改变暂存区和工作区

--hard撤销提交和未提交的修改内容

暂存区和工作区都改变，变为上一次提交

#### ~分离头模式

git checkout 目标不是分支而是具体的提交  提交名或引用则进入分离头模式，HEAD与分支分离

如果进行提交，不会更新分支，当切换到分支时这个提交难以找回

**一般情况下checkout branch 再分支下进行提交**



#### ~本地仓库与远程仓库的同步：

如果本地仓库和远程仓库都有新的提交，（比如直接在github网站上提交，而本地没有)，那么需要先使用git pull（相当于git fetch+git merge) 将远程仓库内容拉取下来并与本地的合并（合并前需要将工作区的内容add commit,防止合并时工作区新内容丢失)，使得本地与远程同步再进行push。

在push之前，可能会产生本地仓库与远程仓库冲突，pull后合并后本地会改变。如果有冲突需要在相关文件内进行选择修改，再add commit 提交最终内容。





