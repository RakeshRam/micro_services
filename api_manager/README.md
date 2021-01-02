# Django Example API Application

Example Django App with REST and Docker(Optional) for a Microservices Architecture.

## <u>Installation</u>

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirments.txt.

From project root DIR run

## <u>Usage(Docker)</u>

```bash
docker-compose up
```

---

## <u>Usage(Manual)</u>

To Set-up environment and dummy data.

```bash
pip install -r requirments.txt
python manage.py makemigrations
python manage.py migrate
python manage.py SetUpData
```

Run server in local environment.

```bash
python manage.py runserver
```

---

## <u>Features</u>

* Basic DRF implementation(CRUD)
  * [Django REST framework](https://www.django-rest-framework.org/)
* App Integrated with Docker(Optional)

---

## <u>API Usage Demo</u>

### **DjangoRestFramework:** `/core/api/`


## License

[MIT](https://choosealicense.com/licenses/mit/)