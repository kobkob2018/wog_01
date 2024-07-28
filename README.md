# World of game

## Welcome to the world of game project from the devOps course!

This project is made for the practice of E2E development, including the ci/cd techniques learned in this course, such as testings, using docker containers, using jenkins pipeline, git and more.

__The actuall app for the exercise is a python script__ that simulates a gaming system, played on the console, with addition of a score view script that shows the user score in a brawser, using flask library.

__To see how to play the actual games__ [click here](#play-the-game)

## Jenkins agent setup

### In order to work with the jenkins pipeline, create a server agent (node) with the following setup:

- __Windows OS:__ The jenkins pipeline includes some "bat" commands, and require Windows OS to commit them.
- __Docker:__ make sure your agent have docker installed and running
- __Create score.txt file:__ In the docker-compise.yml file there is a volume setup for the file "score.txt". Make sure your agent have this file at this path: "/c/jenkins/volumes/wog_data/score.txt"

### If you want to push the image after a successful test, please be sure to set docker credentioals for the agent:

__At the end of the tesing process, the image is being uploaded to docker hub. to do so, folow these 2 steps__

- __Docker login:__ ssh to your agent server, and use the "docker login" command to login to docker hub.
- __Add DOCKER_USERNAME variable to the agent's node in jenkins:__ got to node's configuration, Environment variables and add 'DOCKER_USERNAME'. use your docker username here

#### If the DOCKER_USERNAME variable does not exist, the push to hub step will be skipped, and the image tag will not contain the username prefix.

<a id="play-the-game"></a>

## the games in the world of game:

1. __Memory Game__ - a sequence of numbers will appear for 1 second and you have to guess it back.
2. __Guess Game__ - guess a number and see if you chose like the computer.
3. __Currency Roulette__ - try and guess the value of a random amount of USD in ILS

## Play the game with linux:
- open sh command or cmd
- navigate to the app folder
- sh "python main.py"

These game modules have been meticulously designed to provide an engaging and challenging
experience. Feel free to explore and enjoy the diverse gameplay offered by the World of Games!
