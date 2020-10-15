# Suggestic Code Challenge

Create a web service using any framework that flattens a nested sequence into a single
list of values.

Input:

```
{
"items": [1, 2, [3, 4, [5, 6], 7], 8]
}
```

Output:

```
{
"result": [1, 2, 3, 4, 5, 6, 7, 8]
}
```

You code should be pushed to a public github/gitlab repository.

Extra points:

* Optionally save the result
* Containerize

## Installation

Step 1: Create a virtual environment you can use pyenv or venv or workon in my case used pyenv
```
pyenv virtualenv 3.8.2 test
```

Step 2: Now you may activate de virtual enviroment

```
pyenv activate test 
``` 

Step 3: We must move to the django project folder where we place it
```
cd ChallengeAPIProject/
```

Step 4: Well now we are going to install in the virtual environment the necessary libraries with which this project was built
```
pip3 install -r requirements.txt
```

Step 5: Then we are going to carry out a makemigrations using the django framework
```
python3 manage.py makemigrations 
```

Step 6: execute the following command
```
python3 manage.py migrate
```

Step 7: Then we are going to create superuser
```
python3 manage.py createsuperuser 
```
We put a username and password

Step 8: run server django
```
python3 manage.py runserver
```

Then, we enter the following link of API: http://localhost:8000/api/challenge/

Then, we enter the following link of administrator: http://localhost:8000/admin

The only thing I could not do about the challange is to containerize the application

## Challenge Solution by

* **José Nicolielly** - - [jcnil](https://github.com/jcnil/ChallengeSuggestic)



