# ECE 350/450 Lab Manuals

The lab manuals are hosted [here](https://mistic-lab.github.io/ece-communications-labs/).

If you're a student just looking to complete the labs, go to that link. If you're me in a year trying to remember how to edit this this, or a course TA, or Peter, or a friendly student looking to suggest edits, below shows you how to build it.

## Build instructions

It's built using Jekyll. So if you push changes to master they should auto-publish. You'll need to issue a PR though and it will have to be approved by a mistic-lab admin.

If you want to work on it on your computer to ensure that your proposed changes don't mess everything up, you need to install Jekyll so you can serve it locally. Two obvious options:

1. Install ruby and jekyll (https://jekyllrb.com/docs/)
2. Use a docker container (https://hub.docker.com/r/jekyll/jekyll)
    - I use the following script to run the docker container
    ``` bash
    #!/bin/sh
    IMAGE=jekyll/jekyll
    JEKYLL_VERSION=3.8

    docker run --rm -v "$PWD":/srv/jekyll -it -p 3000:4000 "$IMAGE":"$JEKYLL_VERSION" "$@"
    ```
    - Which is used by

      `$ myScript.sh jekyll serve --watch --drafts`

      where jekyll serve gets you a locally hosted site running at http://localhost:3000/ece350-450-lab-manual/.
