# ICA04 Reflection

## 1. Local and Remote Repositories

What is the difference between the local TaskTrack repository and the repository hosted on GitHub?
- You don't edit the code on GitHub, as it is a Cloud service to host the repo across multiple devices. The local repo is where you make changes and push them out to the public/other developers to work on/view changes from

## 2. Connecting and Pushing

Why did adding `origin` not immediately place the project files on GitHub?
- Adding "origin" only told Git where the remote repository was located. It did not upload any files yet. The project files were still only in the local repository until we ran a push, which sends the commits to GitHub.

## 3. Cloning

How is cloning a repository different from downloading its files as a ZIP archive?
- It keeps track of what changes are currently being tracked at the time of cloning

## 4. Fetching and Pulling

What information did `git fetch` update, and 
what additional action did `git pull` perform?
- A. Current status of the GitHub cloud repo
- B. It took the latest version of the "main" GitHub branch and replaced the local repo with that version's repo

## 5. Focused Commits

Why is it useful to commit the Python feature, sample task data, and README documentation separately?
- It helsps keep seperate features/aspects of the repo easier to understand as they change over time

