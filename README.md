# WebserverProject

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Docker Webserver</h3>


## About The Project
Anarkitty! Order Cloned Kittens
Our webserver allows people to purchase kittens! Customer may choose from 2 different kitten models. The kittens are clones so customers can buy any number of either of the two kittens. To indicate how many they would like, customers simply click the image of the kitten that many times. We have a database on the back-end which stores how many of each kitten the customer would like to purchase. 


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
This project runs on port 10001

To send a curl request and see the message printed, do the following
curl -X POST -d "{<YOUR MESSAGE HERE>}" localhost:10001

IN SUMMARY, do the following
pip install flask --user
pip install Flask-WTF --user
python3 ./Webserver.py
curl -X POST -d "{Wow, this project deserves full credit!}" localhost:10001

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

The application will be running on http://0.0.0.0:10001/

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
