# Django Example API Application

Example Django App using REST, MySQL, Message-Broker and Docker for a Microservices Architecture.

## <u>Installation</u>

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirments.txt.

From project root DIR run

## <u>Usage(Docker)</u>

```bash
docker-compose up --build
```

---

## <u>DB SetUp</u>

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## <u>Usage(Manual)</u>

Set-up Local Environment:

```bash
pip install -r requirements.txt
```

Start local server:

```bash
python manage.py runserver
```

Run MQ Consumer:

```bash
python consumer.py
```

---

## <u>Features</u>

* Demo Super Heros Admin Page
  * `http://localhost:8000/`
* Basic DRF implementation(CRUD)
  * [Django REST framework](https://www.django-rest-framework.org/)
* RabbitMQ integration for message-broker.
  * [CloudAMQP](https://www.cloudamqp.com/)
* App Integrated with Docker
* App Integrated with Kubernetes. [Instructions](k8s/README.md)

---

## <u>API Usage Demo</u>

### **DjangoRestFramework:** `/api/`

* **Query Characters Record -> GET**

  ```javascript
  /api/characters/
  /api/characters/<CHARACTER-ID>/
  ```

* **Create New Characters -> POST**

  ```JAVASCRIPT
  /api/characters/
  ```

  Example:

  ```javascript
  {
    "name": "Iron Man",
    "series": "Marvel",
    "team": "Avengers",
    "origin": "NewYork",
    "ability": [
      {
        "ability": "Speed"
      },
      {
        "ability": "Strength"
      }
    ],
    "creator": {
      "name": "Stan Lee", 
      "country": "US"
    }
  }
  ```

* **Update Character Record -> PUT**

  ```javascript
  /api/characters/<CHARACTER-ID>/
  ```
  
* **Delete Character -> DELETE**

  ```javascript
  /api/Characters/<CHARACTER-ID>/
  ```

## License

[MIT](https://choosealicense.com/licenses/mit/)