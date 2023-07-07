*test

# Temp repository to learn library FastAPI

This is application for monitoring users and trades. Without realy data, it contains method adding new user. Every person has a few statuses, like superuser, verified or active. Moreover, user can have achievement in trade-grades or degree past buying or selling. Project is related to PostgreSQL by _sqlalchemy_ and _alembic_ . To see and use api you need to build server with _uvicorn_

### Get Started

Create virtual environent and install requirements with pip
```sh
cd fast-API-learning
python -m venv venv
venv/Scripts/activate.bat #for windows
pip install -r requirements.txt
```

### Build server
Create server by uvicorn
```sh
uvicron main:app --reload
```
Enjoy application with api!

### Contacts

| Service | Link |
| ------ | ------ |
| VK | [cradm_lozzer](https://vk.com/cradm_lozzer)  |
| TG | [cradm_lozzer](https://t.me/cradm_lozzer)  |