*test

# Temp repository to learn library FastAPI

This is application for monitoring users and trades. Without really data, it contains method adding new user. Every person has a few statuses, like superuser, verified or active. Moreover, user can have achievement in trade-grades or degree past buying or selling. Project is related to PostgreSQL by _sqlalchemy_ and _alembic_ . To see and use api you need to build server with _uvicorn_

### Get Started

Go to folder
```sh
cd fast-API-learning
```

Create and activate virtual environment
```sh
python -m venv venv
venv/Scripts/activate.bat #for windows
```

Install dependencies
```sh
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