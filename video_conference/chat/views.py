from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone
from .models import MyFile
import uuid
from django.shortcuts import get_object_or_404
from chat.models import MyFile
# print(MyFile.objects.values_list('id', flat=True))
# See all entries

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {'success': "Registration successful. Please login."})
        else:
            error_message = form.errors.as_text()
            return render(request, 'register.html', {'error': error_message})

    return render(request, 'register.html')

def file_sharing(request):
    if request.method == 'POST':
        userfile=request.FILES.get('userfile')
        print(userfile)
        if userfile:
            id=str(uuid.uuid4())
            file = MyFile(id=id, file=userfile)
            file.save()
            link = "http://127.0.0.1:8000/"+str(id)+"/"
            print(link)
            return render(request, 'file.html', {'link': link})
    all_files = MyFile.objects.all()
    
    return render(request, 'file.html', {'all_files': all_files})
import os
from django.conf import settings
from django.http import FileResponse
def downloadFile(request, id):
    print(id)
    id=str(id).lower()
    get_file = get_object_or_404(MyFile, id=id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(get_file.file))  # Ensure full path
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    else:
        return render(request, 'error.html', {'message': 'File not found'})
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            request.session['login_time'] = datetime.datetime.now().isoformat()  # Store login time
            return redirect("/dashboard")
        else:
            return render(request, 'login.html', {'error': "Invalid credentials. Please try again."})

    return render(request, 'login.html')

# @login_required
# def attendance_view(request):
#     login_time = request.session.get('login_time', None)
    
#     # If there's no login time, return an error message
#     if login_time is None:
#         return render(request, 'attendance.html', {'error': 'Login time not found.'})

#     # Calculate session duration (time passed since login)
#     try:
#         login_time_obj = datetime.datetime.fromisoformat(login_time)
#         current_time = datetime.datetime.now()
#         session_duration = current_time - login_time_obj

#         # Check if session duration is more than 20 minutes
#         session_status = "Present" if session_duration.total_seconds() > 1200 else "Not Present"
        
#         # Prepare the session duration in the desired format
#         formatted_duration = str(session_duration).split('.')[0]  # HH:MM:SS

#         # Store the session data in a text file
#         current_date = current_time.strftime("%Y-%m-%d %H:%M:%S")

#         # Store the session data in a text file
#         username = request.user.username
#         with open("session_data.txt", "a") as file:
#             file.write(f"Date: {current_date}, Username: {username}, Session Duration: {formatted_duration}, Status: {session_status}\n")

#         # Send the session info to frontend for real-time updates
#         context = {
#             'session_duration': formatted_duration,
#             'session_status': session_status,
#             'login_time': login_time  # Send login_time for JavaScript to calculate real-time
#         }

#     except ValueError:
#         session_duration = None
#         session_status = "Invalid time format"
#         context = {'error': 'Invalid time format'}

#     return render(request, 'attendance.html', context)
@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.first_name})
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json

@csrf_exempt  # Use @csrf_exempt to allow POST requests from the frontend
def save_session_duration(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_name = data.get('userName')
        duration = data.get('duration')

        if user_name and duration is not None:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            formatted_duration = str(datetime.timedelta(seconds=duration))

            # Save session data to text file
            with open("session_data.txt", "a") as file:
                file.write(f"Date: {current_date}, Username: {user_name}, Session Duration: {formatted_duration}\n")

            return JsonResponse({"message": "Session saved successfully!"})
        else:
            return JsonResponse({"error": "Invalid data!"}, status=400)

@login_required
def videocall(request):
    login_time = request.session.get('login_time', None)
    
    # If there's no login time, return an error message
    # if login_time is None:
    #     return render(request, 'attendance.html', {'error': 'Login time not found.'})

    # Calculate session duration (time passed since login)
    try:
        login_time_obj = datetime.datetime.fromisoformat(login_time)
        current_time = datetime.datetime.now()
        session_duration = current_time - login_time_obj

        # Check if session duration is more than 20 minutes
        session_status = "Present" if session_duration.total_seconds() > 1200 else "Not Present"
        
        # Prepare the session duration in the desired format
        formatted_duration = str(session_duration).split('.')[0]  # HH:MM:SS

        # Store the session data in a text file
        current_date = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # Store the session data in a text file
        username = request.user.username
        with open("session_data.txt", "a") as file:
            file.write(f"Date: {current_date}, Username: {username}, Session Duration: {formatted_duration}, Status: {session_status}\n")

        # Send the session info to frontend for real-time updates
        # context = {
        #     'session_duration': formatted_duration,
        #     'session_status': session_status,
        #     'login_time': login_time  # Send login_time for JavaScript to calculate real-time
        # }

    except ValueError:
        session_duration = None
        session_status = "Invalid time format"
        context = {'error': 'Invalid time format'}
    return render(request, 'videocall.html', {'name': request.user.first_name + " " + request.user.last_name})

@login_required
def logout_view(request):
    logout(request)
    return redirect("/login")

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'joinroom.html')
