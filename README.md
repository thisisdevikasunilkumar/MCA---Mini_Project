# Procezo

**Procezo** is an Employee Monitoring and Productivity Management System designed to automate attendance, track work activities, and evaluate employee engagement through real-time emotion detection and analytics.

---

## 🚀 Features

### 👨‍💼 Admin Module
- **Manage Employees:** Add, edit, and manage employee profiles.
- **Attendance Monitoring:** Automated attendance logging via face recognition.
- **Emotion Tracking:** Monitor employee emotions and stress levels during working hours.
- **Activity Reports:** Analyze productivity through keyboard and screen activity monitoring.
- **Centralized Dashboard:** View consolidated insights of performance, attendance, and engagement metrics.

### 👩‍💻 Staff Module
- **Automated Login/Logout:** Attendance recorded using facial recognition.
- **Emotion Detection:** Real-time emotion analysis during active work sessions.
- **Profile Management:** Employees can update personal information.
- **Performance Reports:** View personal productivity summaries and attendance logs.

---

## 🧰 Technologies Used

| Component              | Technology                                                       |
|------------------------|------------------------------------------------------------------|
| **Front-End**          | HTML, CSS, JavaScript                                            |
| **Back-End**           | Python (Django Framework)                                        |
| **Database**           | MySQL                                                            |
| **Server**             | Apache / WAMP                                                    |
| **AI Module**          | Convolutional Neural Network (CNN) for Face & Emotion Detection  |
| **Tools**              | VS Code                                                          |
| **Operating System**   | Windows 7 or above                                               |
| **Supported Browsers** | Chrome, Firefox, Internet Explorer                               |

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/thisisdevikasunilkumar/MCA---Mini_Project.git


2. **Set Up the Database**
   - Import the provided `.sql` file into **MySQL**.

3. **Configure Django**
   - Open `settings.py` and update:
     
   ```bash
   DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
     }
   }

4. **Run Migrations**
   ```bash
     python manage.py makemigrations
     python manage.py migrate

5. **Start the Server**
   ```bash
    python manage.py runserver

4. **Access the Application**
   - Open in your browser:
     
   ```bash
     http://127.0.0.1:8000/
   
---   

## 👥 Team Members
- [Devika Sunilkumar](https://github.com/thisisdevikasunilkumar)
- [Diya V P](https://github.com/diyaprince)
- [Hitha Krishna P R](https://github.com/HithaKrishna)
- [Tina Paul C](https://github.com/tinachirammal2002)

---

### 📌 Note
This project was developed as part of the **MCA 3rd Semester Mini Project** and is intended purely for learning and academic purposes.
