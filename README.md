# 📧 Email Scheduler App

A Python-based Email Scheduler that allows you to schedule emails at a future time using Celery and Redis. The application is fully containerized with Docker and super easy to use — just provide your Gmail App Password and you're good to go!

---

## 🚀 Features

- ✅ Schedule emails with custom subject, body, and delivery time.
- 🕒 Tasks are handled asynchronously using **Celery** with **Redis** as the message broker.
- 🐳 Fully Dockerized for seamless deployment.
- 🔐 Uses secure Gmail App Password (no need to store your actual password).
- 💬 Simple and user-friendly interface.

---

## 🛠 Tech Stack

- Python 3
- Flask
- Celery
- Redis
- Docker / Docker Compose
- SMTP (for Gmail email sending)

---

## 📦 Installation (Without Docker)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Keerthi11123/email-scheduler.git
   cd email-scheduler
