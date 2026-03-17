# ShowMyData
Simple application to upload, list, and delete files with basic password authentication.

---

## Requirements
* Python 3.10+
* Node.js 18+
* npm or yarn

---

# Backend
Navigate to the folder called "backend"

## 1. Create virtual environment

```bash
pip install virtualenv
```

```bash
python -m virtualenv venv
```

### Activate environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / Mac:**

```bash
source venv/bin/activate
```

---

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Run script to add initial password:

```bash
python initial_config.py
```

Server available at: [http://localhost:8000](http://localhost:8000)

---

# Frontend (React + Vite)
Navigate to the "frontend" folder

## 1. Install dependencies

```bash
npm install
```

---

Navigate to the "show-my-data" folder

## 2. Install dependencies

```bash
npm install
```

---

Frontend available at: [http://localhost:5173](http://localhost:5173)

---

## Start service:
Double-click the file start_app.bat inside "show_my_data"

## Features
* Upload files
* List files
* Search files
* Select multiple files
* Delete selected files

---

## Important notes
* Authentication is basic (no JWT)
* There is no real endpoint protection
* Passwords are stored in plain text
