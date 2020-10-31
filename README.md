# WebserverProject

<!-- PROJECT LOGO -->
<img align="center" src="./Static/images/standingCat.jpg">

<br />
<p align="center">
  <h3 align="center">Docker Webserver</h3>

  
<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Description](#description)
* [Built With](#built-with)
* [Usage](#usage)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)


## Description
Anarkitty! Order Kittens

For years individuals have longed for soft cuddly companions. For the first time in history it is now possible to have kittens delivered to your doorstep with a click of a button. No more lonely nights with no comforting kitten purs. No more lifeless afternoons. At Anarkitty we care about our customers' kneads. We only serve the finest grass fed organic kittens, to quality kitten control.

Our webserver allows people to purchase kittens! Customer may choose from 2 different kitten models. Customers can buy any number of either of the two kittens. To indicate how many they would like, customers simply click the image of the kitten that many times. We have a database on the back-end which stores how many of each kitten the customer would like to purchase. 

## Built with

Our project uses a small collection of developer tools to power a world with kittens for everyone. Our tools include.

* [Python3](https://docs.python.org/3/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/m)
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)
* [Docker](https://www.docker.com/)
* [Github](https://github.com/)


## USAGE
Ensure that flask is currently installed
```sh
pip install flask --user
pip install Flask-WTF
```
Run the program
```sh
python3 ./Webserver.py
```
This project runs on port 5000

To send a curl request and see the message printed, do the following
``` sh
curl -X POST -d "{<YOUR MESSAGE HERE>}" localhost:5000
```

You will recieve an index.html from the curl request with our front end written in html. You should see the message from the curl request in the same terminal that you run the program in. Note you will not see the message when running the project in docker. 

## DOCKER
To run the program in a docker container run the following commands.

```sh
git clone https://github.com/wjepsen/WebserverProject
```
```sh
docker image build -t flaskwebserver .
```
```sh
docker run --env FLASK_APP=Webserver.py -p 127.0.0.1:10001:10001 -d flaskwebserver
```
``` sh
curl -X POST -d "{<YOUR MESSAGE HERE>}" localhost:10001
```

The application will be running on http://0.0.0.0:10001/


To send a curl request to the dockerized webserver use the following command.
``` sh
curl -X POST -d "{<YOUR MESSAGE HERE>}" localhost:10001
```

## Contact

If you would like to provide feedback or order any kittens over the phone please call 1-800-ANARCAT

# Acknowledgements

We would like to thank Dr. Pallickara, Caleb Carlson, and our cats Casper, Payton, Weebo and Albert. 

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
