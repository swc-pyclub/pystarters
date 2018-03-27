# Introduction to Version Control

The ability to record and keep track of the history of changes in your evolving codebase is a *fundamental* skill for any modern software development pipeline.

The goal of this worksheet is to show you easy it is to get started, and give you a flavor of some of the benefits of using Version Control for all your code development.

## Installation

Version control requires storing extra data together with your files to keep track of the version history. This is known as a repository. There are several well-established tools and pipelines for automating the process of managing version control repositories.

For this introduction, we will focus exclusively on [Git](https://git-scm.com/), which is arguably the most popular solution for open-source development.

1. Install the [SourceTree](https://www.sourcetreeapp.com/) version control client.

SourceTree is a graphical user-interface for the Git version control system, which will allow you to create and manage local Git repositories on your computer.

Another important aspect of version control is the possibility of storing and sharing repositories online. This allows you to access your code from multiple computers, or collaborate with other developers on common software projects.

Again, there are several established solutions for hosting and sharing version control repositories. For this introduction we will be using [GitHub](https://github.com/), which has become the standard for sharing and collaborating on open-source projects.

2. Go to the GitHub website and create a new personal account.

Now you are ready to create your first version control repository.

## Creating a new repository

You can create a new repository either from an existing folder in your local drive, or directly online from the GitHub website.

3. On the GitHub website, create a [new](https://github.com/new) repository.

As a rule of thumb, you should always have a README.md file and a license on any public repository.

### README file

The README.md (md stands for [Markdown](https://daringfireball.net/projects/markdown/)) file is a text file containing a short description of your repository, what it contains, and how it can be used.

It may feel like this is a lot of work, having to explain to others what you are doing. However, the best way to think about it is that you are actually explaining it to yourself 6-months from now, when you are very likely to have entirely forgotten what you were doing today.

**In a very real way, version control is all about writing good letters to your future self.**

### Project License

If your repository is hosted online, there is some probability that it will be noticed by others who may be interested in your code. It is important to make it clear to them how you want your code to be used.

There are a number of tried and tested open-source project licenses that you can choose from. It is important to clarify your intentions regarding the code, even if you don't care how it is ultimately used.

The most popular open-source licenses are the [GPL](https://en.wikipedia.org/wiki/GNU_General_Public_License) and the [MIT License](https://en.wikipedia.org/wiki/MIT_License). Most other variants have been derived from principles that were established by these two.

There is a very heated discussion about whether to use one or the other that we will entirely sidestep for the purposes of this discusion. However, in case of doubt, we recommend the MIT license because of its simplicity.

## Your first commit

Now that your repository is created, you can work with it as you would with any other folder in your computer.

If you created the repository online, you can *pull* a copy of the repository to your computer so that you can work with it locally.

4. Connect your GitHub account with SourceTree using the [Accounts](https://confluence.atlassian.com/get-started-with-sourcetree/connect-your-bitbucket-or-github-account-847359096.html) menu.

5. Clone the online repository that you have just created using the [Remote](https://confluence.atlassian.com/get-started-with-sourcetree/clone-a-remote-repository-847359098.html) menu.

You should now have a local copy of the repository in your computer (including the README.md and license files).

6. Open the README.md file and make some changes. Consider learning the [markdown syntax](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) in the process.

Now that you have made some changes, you need to indicate to the version control system that you are ready to *commit* these changes to the repository.

This is the main difference between a version control system and a cloud-based backup storage system like Dropbox: in cloud-storage, backups of your files are kept individually so you can go back to them in case any mistakes happen.

However, these systems have no idea which changes go together. It is often the case in software development that in order to get something done you actually need to change multiple files. Furthermore, which part of the file was actually changed, and what the change exactly means is critical, since code can be hard to read by itself.

In a version control system, this issue is handled explicitly: *you* tell the version control which files were changed and how they go together by creating a *commit*. Each commit requires a set of changes and a message that describes what those changes accomplished.

**Writing good commit messages is the most fundamental, and most difficult, step in version control.**

It is hard to learn because you will only likely feel the first benefits of good commit messages potentially months later. With practice, you will come to understand other advantages as you integrate good writing into your daily coding routine.

7. Create a new commit from your local changes using the [Commit](https://confluence.atlassian.com/sourcetreekb/commit-push-and-pull-a-repository-on-sourcetree-785616067.html) button on SourceTree.

Congratulations, you have just made your first commit!

## Synchronizing remote repositories

Now that you have committed some local changes, the history of your repository is different between your local copy and the remote hosted on GitHub.

In order to synchronize changes with your remote repository, you have to *push* your changes to the remote. Conversely, if there were new changes in the online repository (e.g. you worked across different computers), you would want to *pull* those changes locally.

8. Synchronize your local changes with your remote repository using the [Push](https://confluence.atlassian.com/sourcetreekb/commit-push-and-pull-a-repository-on-sourcetree-785616067.html) button on SourceTree.

9. Go to the GitHub website for your repository and confirm that your changes have been successfully stored.

That's it, you have now learned the basics of version control. The most important next step is to actually integrate it into your routine development pipeline and start realizing by yourself why it is so useful.
