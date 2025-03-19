# DRF Quiz & Blog API

This is a Django REST Framework (DRF) based API project that provides functionalities for a quiz and blogging platform. It includes user authentication, quiz creation, question-answer handling, blog management, and leaderboard tracking.

## Features
- User authentication (Sign up & Login)
- Category-based quiz management
- Question and choice creation
- Answer submission with score tracking
- Blog system with category filtering
- Leaderboard for top-performing users
- Django Admin panel for content management

## Installation

### Prerequisites
- Python 3.x
- Django 5.x
- Django REST Framework

### Setup Instructions

1. Clone the repository:
   ```sh
   git clone https://github.com/robiulsunnyemon/CodeAlpha_FlashcardQuiz_App.git
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```
7. Access the API at:
   ```
   http://127.0.0.1:8000/api/
   ```

## API Endpoints

### Authentication
- `POST /api/auth/signup/` - Register a new user
- `POST /api/auth/login/` - Login and receive a token

### Questions & Answers
- `GET /api/questions/` - Retrieve all questions
- `POST /api/questions/` - Create a new question
- `GET /api/questions/category/<int:category_id>/` - Get questions by category
- `GET /api/choices/question/<int:question_id>/` - Get choices for a question

### Blogs
- `GET /api/blogs/` - Retrieve all blogs
- `POST /api/blogs/` - Create a new blog
- `GET /api/blog/category/<int:category_id>/` - Get blogs by category

### Leaderboard
- `GET /api/student_leaderboard/` - Retrieve student leaderboard

## Database Models

### Quiz Models
- **Categoryquestion**: Stores quiz categories
- **Question**: Stores questions linked to categories
- **Choice**: Stores multiple-choice options for questions
- **QuestionAnswer**: Stores user-submitted answers and scores

### Blog Models
- **CategoryBlog**: Stores blog categories
- **Blog**: Stores blog posts linked to categories and users

### User Details
- **UserDetails**: Stores additional user information (name, country, phone number)

## Admin Panel
Access the Django admin panel at:
```
http://127.0.0.1:8000/admin/
```
Use the superuser credentials created earlier to log in.

## Flutter App Integration
This project is also used as a backend for a Flutter application. The Flutter app follows **Clean Architecture** and uses **Flutter BLoC** for state management.

### Flutter App Features
- **State Management**: BLoC pattern for efficient state handling.
- **Modular Architecture**: Clean separation of concerns using Clean Architecture principles.
- **API Integration**: The app connects with this Django REST API to fetch quiz questions, blogs, and user details.

### Setup Instructions for Flutter
1. Clone the Flutter app repository:
   ```sh
   git clone https://github.com/robiulsunnyemon/CodeAlpha_FlashcardQuiz_App.git
   cd futter
   ```
2. Install dependencies:
   ```sh
   flutter pub get
   ```
3. Run the app:
   ```sh
   flutter run
   ```

## Deployment
- Ensure `DEBUG = False` in `settings.py`
- Set up a production database (PostgreSQL recommended)
- Configure static and media files handling
- Use a production-ready web server like Gunicorn with Nginx

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is open-source and available under the MIT License.

