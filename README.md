# 📦 Weather Python Application

A simple Python Flask application that fetches real-time weather information using the OpenWeather API. This project is built for learning **Python**, **Docker containerization**, and **GitHub workflows**.

---

## 🚀 Features

* Real-time weather lookup
* Flask + HTML template front-end
* Dockerized application
* API key support using environment variables
* Ready for CI/CD using GitHub Actions

---

# 📁 Project Structure

```
weather-python/
│── app.py
│── requirements.txt
│── Dockerfile
│── templates/
│     └── index.html
│── README.md
```

---

# 🐍 1. Run Locally (Python)

### Create and activate virtual environment

```bash
python -m venv venv
.\venv\Scripts\activate    # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Set API Key (OpenWeather)

```bash
$env:WEATHER_API_KEY="your_api_key_here"
```

### Run the application

```bash
python app.py
```

App runs at:

👉 [http://localhost:5000](http://localhost:5000)

---

# 🐳 2. Run with Docker

### Build Docker image

```bash
docker build -t username/weather-app:latest .
```

### Run container

```bash
docker run -p 5000:5000 -e WEATHER_API_KEY=your_api_key username/weather-app:latest
```

App available at:

👉 [http://localhost:5000](http://localhost:5000)

---

# 📝 3. Git Commands (Push to GitHub)

### Initialize Git

```bash
git init
```

### Add and commit

```bash
git add .
git commit -m "Initial commit"
```

### Rename branch to main

```bash
git branch -M main
```

### Add remote origin

```bash
git remote add origin <your-repo-url>
```

### Push to GitHub

```bash
git push -u origin main
```

### If push is rejected due to history difference

```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

---

# 🔑 Environment Variables

| Variable          | Description                  |
| ----------------- | ---------------------------- |
| `WEATHER_API_KEY` | Your OpenWeather map API key |

---

# 🛠️ 4. Dockerfile (used for building image)

```dockerfile
FROM python:3.10-slim
ARG WEATHER_API_KEY
ENV WEATHER_API_KEY=$WEATHER_API_KEY
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

---

# ❤️ Contributing

Feel free to fork the repo and submit pull requests.

---

# 📧 Support

For any issues, open a GitHub issue in this repository.
