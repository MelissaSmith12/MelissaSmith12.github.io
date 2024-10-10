# MelissaSmith12.github.io

Basically, see the instructions in this resource: https://spapas.github.io/2013/10/07/pelican-static-windows/

I renamed pelrun to pelgeneratecontent

## Local Development

```powershell
pip install pelican Markdown
.\pelgencontent.bat # run a build
.\pelserve.bat # serve the build
```

## Deployment

Anything merged to master will be deployed automatically.

```powershell
git status # confirm you're on correct branch
git checkout -b branch-name # create a new branch if needed
git add . # stage all changes
git status # confirm all changes are staged
git commit -m "message" # commit changes
git push --set-upstream origin branch-name # push changes
```

Now you can go to github.com and create a pull request from
your new branch to master. This will allow you to see if
the site builds successfully before merging to master and
triggering a deploy.

## Todo

- [ ] Support darkmode
- [ ] Fix favicon
- [ ] Update, remove, or replace Google Analytics
- [ ] Add Bluesky, YouTube, Patreon to social charms