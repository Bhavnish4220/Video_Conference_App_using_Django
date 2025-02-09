
# Video Conferencing and File Sharing Web Application

This is a web-based application built with Django and integrated with **ZEGOCLOUD** for real-time video conferencing. The application also provides **file sharing** capabilities to allow users to exchange files during live meetings.

## Features

- **Real-Time Video Conferencing**: Powered by ZEGOCLOUD, the app allows users to join virtual rooms, make video and audio calls, and share screens.
- **File Sharing**: Users can upload and download files during the conference.
- **User Authentication**: Secure login and registration system using Django's built-in authentication.
- **Attendance Tracking**: Tracks student attendance based on their login duration and marks them as present or absent.
- **Responsive UI**: The frontend is designed using HTML, CSS, and JavaScript to ensure compatibility across devices.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Video Conferencing**: ZEGOCLOUD API
- **Database**: SQLite (for development) or PostgreSQL (for production)
- **Authentication**: Django Authentication System
- **File Uploads**: Django File Storage

## Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/video-conferencing-webapp.git
cd video-conferencing-webapp
```

### 2. Create a Virtual Environment (Optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up ZEGOCLOUD
1. Sign up at [ZEGOCLOUD](https://www.zegocloud.com/).
2. Obtain the **AppID** and **AppSecret**.
3. Update the settings in `settings.py` with your ZEGOCLOUD credentials.

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Start the Development Server
```bash
python manage.py runserver
```

### 7. Access the Application
Open your browser and go to `http://127.0.0.1:8000/` to start using the app.

## Usage

1. **Login/Register**: Create an account or log in to the application.
2. **Create a Room**: Create a video conference room and invite others to join using the room ID.
3. **Join a Room**: Use the room ID to join an ongoing meeting.
4. **Share Files**: Upload files to share with participants in the room.



## Acknowledgements

- [ZEGOCLOUD API](https://www.zegocloud.com/) for providing real-time video conferencing capabilities.
- Django for powering the backend of the application.
