# Kalwak Portfolio Webpage

Kalwak online webpage. This is the portfolio of Kalwak, made to give
general information to the public, specific information such as products or
showcase older proyects, or to order a product. The website is [Kalwak](http://kalwak.xyz/).
This repository is in bitbucket (for the telegram integration) and github (an open source copy).


### Prerequisites

- graphviz
- postgresql
- nodejs
- npm
- python 3.7


### Installing

Clone this repository

```
git clone https://github.com/Kalwak/Kalwak_Portfolio
cd Kalwak_Portfolio
```

Create a virtual environment

```
mkdir ~/.virtualenvs
virtualenv -p python3 ~/.virtualenvs/kalwak_portfolio
source ~/.virtualenvs/kalwak_portfolio/bin/activate
```

Install python requirements

```
cd Portfolio
pip install -r requirements.txt
```

## Creating the Data Base

In order to create the data base

```
sudo -u postgres createdb kalwak
```

This is asumming you already have the user postgres and want to use kalwak as 
a name for the data base, as it is for default, otherwise just change the 
variable in the .env


## Setting up environment variables

To set up your env variables you should create a .env in Portfolio/Portfolio
and add your variables as in the .env.example

## Models Django and Postgres

To create all the django models in the data base

```
python manage.py makemigrations
python manage.py migrate
```

## Running tests

To run all the unittets

```
python manage.py test
```

## Deployment

First off run the following command if you need to make a frontend
build of vuejs.


```
npm run build
```

this makes a dist directory where the compiled frontend code resides.
After the build has been made remove the files in the backend folder called

frontend/static/  and frontend/templates/

now add the static files from the dist folder to frontend/static/ and
move the index.html from the dist folder to the frontend/templates/ folder.
 

## Built With

* [Django](https://www.djangoproject.com/) - The BackEnd framework
* [Vuejs](https://vuejs.org/) - The FrontEnd framework


## Authors

* **Edwin Garcia** - *Frontend Development* - [Edwing123](https://github.com/Edwing123)
* **Joseph Zamora** - *Lead Programmer* - [JZ1999](https://github.com/JZ1999)
* **Jose Quesada** - *Backend Development* - [josemarioqv](https://github.com/josemarioqv)



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
