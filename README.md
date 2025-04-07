# 💬 Heap Overflow

**Heap Overflow** is a parody of Stack Overflow, designed as a Q&A website where developers can authenticate to share knowledge, ask questions, and follow topics of interest. This project was built to demonstrate expertise in web development, particularly with Django and Python.

## ✨ Features

- **User Authentication** — Secure signup, login, and logout functionality.
- **Ask & Answer Questions** — Authenticated users can post and respond to programming questions.
- **Topic Following** — Users can follow specific topics and technologies.
- **Search & Filter** — Easily find questions or browse by topic.
- **Responsive UI** — Clean, mobile-friendly design with Bootstrap.

## 🛠️ Tech Stack

**Frontend:**
- HTML, CSS
- Bootstrap

**Backend:**
- Python
- Django

**Database:**
- SQLite (development)
- PostgreSQL (production)

**Deployment:**
- Heroku

## 🧪 Local Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/blakebrandon-hub/heap-overflow.git
   cd heap-overflow


## Installation

To set up Heap Overflow locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/blakebrandon-hub/heap-overflow.git
   cd heap-overflow
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Deployment

Heap Overflow is hosted on Heroku. To deploy your own instance:

1. **Set Up a Heroku Account**:
   - Create a Heroku account at [https://www.heroku.com/](https://www.heroku.com/).

2. **Install the Heroku CLI**:
   Follow the [Heroku CLI documentation](https://devcenter.heroku.com/articles/heroku-cli) to install.

3. **Deploy to Heroku**:
   ```bash
   heroku login
   heroku create heap-overflow
   git push heroku main
   heroku run python manage.py migrate
   ```

4. **Configure Environment Variables**:
   Set the necessary variables such as `SECRET_KEY`, `DEBUG`, and database credentials using the Heroku dashboard or CLI.
   
## Contact

- **Author**: Blake Brandon
- **Email**: [blakebrandon.dev@gmail.com](mailto:blakebrandon.dev@gmail.com)

