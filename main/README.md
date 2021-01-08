# Flask Example UI Application

Example Flask UI App with REST, MySQL, Message-Broker and Docker for a Microservices Architecture.

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
python manager.py db init
python manager.py db migrate
python manager.py db upgrade
```

---

## <u>Usage(Manual)</u>

Set-up Local Environment:

```bash
pip install -r requirements.txt
```

Start Local Server:

```bash
python ui_interface/main.py
```

Run MQ Consumer:

```bash
python ui_interface/producer.py
```

---

## <u>Features</u>

* Demo Super Heros Gallery with vote button.
  * Docker `http://localhost:8001/`
  * Manual `http://localhost:5000/`
* App Integrated with Docker(Optional)

---

## License

[MIT](https://choosealicense.com/licenses/mit/)