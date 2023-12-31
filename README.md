# Earn Golden
Manage your earnings with this API support. This API has a focus to an application to help you to manage
your money, about earnings and how you use it in your life.

A lot of people around the world hasn't financial education, Brazil unhappy is at this role. But with
this application, it would be possible to manage what you do and want to do to your own money by
yourself.

## Summary
- [Dependencies](#dependencies)
- [Models](#models)
  - [Detailed Models](#detailed-models)
- [Migrations](#migrations)
- [How to Run](#how-to-run)
- [Database Relationship](#database-relationship)
- [Project FAQ](#project-faq)

## Dependencies
This project is build with MVC and Python Programming Language. But we have some additional packages like:

- Alembic
- Python 3
- Pip
- Pydantic
- SQL Alchemy
- FastAPI
- Uvicorn
- Requests
- BeautifulSoup4
- Docker
- Docker Compose >= 2.21.0

## Models
This is basically our models to use with intent of access the backend of this application. Here it
is represented as a `.json` format. Basically we have the following models:

1. Account
2. Bank
   1. Card
   2. Invoice
   3. Transfer
   4. Pix
3. MoneyBox
4. Deposit
5. Payment

### Detailed Models
For each one of previous models list, the following `.json` type is indicated. We present to you
each model with their attributes:
> Account Model
```json
{}
```
> Bank Model
```json
{}
```
> Card Model
```json
{}
```
> Invoice Model
```json
{}
```
> Transfer Model
```json
{}
```
> Pix Model
```json
{}
```
> MoneyBox Model
```json
{}
```
> Deposit Model
```json
{}
```
> Payment Model
```json
{}
```

## Migrations
To run this app you need to have a migration structure. You can generate
it running the module [set_alembic.py](set_alembic.py) or if there's
in this project, I may to recommend see: [How to Migrate](#how-to-migrate)
in FAQ.

## How to Run
To run this application, just copy and paste:
```commandline
uvicorn app:app --reload
```

## Database Relationship
> **TO-DO**

## Project FAQ
Here we've a FAQ about this project.

<details id="how-to-migrate">
    <summary>
        How to Migrate?
    </summary>
    <ul>
        <caption>Creating A Migration:</caption>
        <li><code>alembic revision --autogenerate "migration_phrase"</code></li>
        <caption>Running a Migration:</caption>
        <li><code>alembic upgrade head</code></li>
        <caption>You can swap to a version:</caption>
        <li><code>alembic upgrade 73d4b45005c5</code></li>
    </ul>
</details>

<details id="install-dependencies">
    <summary>
        How To Install Dependencies?
    </summary>
    <ul>
        <li>Generate a venv python, so:</li>
        <li><code>pip install -r requirements.txt</code></li>
    </ul>
</details>

<details>
    <summary>How To Install Docker and Docker Compose?</summary>
    <caption>Linux OS</caption>
    <li><code>sudo curl -L "https://github.com/docker/compose/releases/download/3.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose</code></li>
    <li><code>sudo chmod +x /usr/local/bin/docker-compose</code></li>
    <li><code>sudo usermod -aG docker $USER</code></li>
</details>

<details>
    <summary>How To Run or Stop Docker Compose?</summary>
    <caption>To Run Docker:</caption>
    <li><code>docker-compose up -d</code></li>
    <caption>To Stop Docker:</caption>
    <li><code>docker-compose down</code></li>
</details>

[back to doc init](#earn-golden)
