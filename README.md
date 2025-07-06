# StudyTogether
Django Room Chat Application
Overview
This is a Django-based web application that allows users to create and manage chat rooms, post comments, and view participants. Users must be authenticated to create rooms, post comments, or delete their own comments (or those in rooms they host). The application features a modern, colorful UI with scrollable comment and participant sections, styled using Tailwind CSS.
Features

Room Creation: Users can create rooms with a topic, name, and description.
Comment System: Authenticated users can post and delete comments in rooms.
Participant Tracking: Automatically adds comment authors to room participants.
Authorization: Only comment authors or room hosts can delete comments.
Responsive Design: Scrollable sections for comments and participants, with a gradient background and frosted glass effect.
Error Handling: Displays validation errors for empty inputs or unauthorized actions.

# Requirements

Python 3.8+
Django 4.x or 5.x
SQLite (default) or other database supported by Django
Tailwind CSS (via CDN)

#  Setup Instructions
1. Clone the Repository
git clone https://github.com/sophonie-1/StudyTogether.git
cd StudyTogether 

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install django

4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Create a Superuser
python manage.py createsuperuser

6. Run the Development Server
python manage.py runserver

7. Access the Application

Open http://127.0.0.1:8000 in your browser.
Log in with the superuser credentials or register a new user (if registration is implemented).

#  Project Structure
project/
├── myapp/
│   ├── migrations/
│   ├── templates/myapp/
│   │   ├── components          # Room view with comments and participants
│   │   ├── myapp
        |--registration    # Form for creating rooms
│   ├── __init__.py
│   ├── admin.py
│   ├── forms.py              # MessageForm and RoomForm
│   ├── models.py             # RomModel, MessageModel, TopicModel
│   ├── urls.py               # URL routes
│   ├── views.py              # CreateRoomView, RomeView
├── manage.py
├── README.md

#  Models

TopicModel: Stores topics (topic_name).
RomModel: Represents rooms (host, topic, name, description, participants, created, updated).
MessageModel: Represents comments (user, rom, body, created).

#  Views

CreateRoomView (CreateView):
Handles room creation with RoomForm.
Assigns topic (via get_or_create) and host (logged-in user).
Redirects to home-view on success.


RomeView (CreateView):
Displays room details, comments, and participants.
Handles comment creation (MessageForm) and deletion (action=delete).
Enforces authorization for comment deletion.



#  Templates

rom.html:
Displays room details, scrollable comments, and participants.
Styled with Tailwind CSS (gradient background, purple buttons, frosted glass effect).
Auto-scrolls to the latest comment and participant.


room_form.html:
Form for creating rooms with topic, name, and description.
Matches the colorful, modern design of rom.html.



URLs
In myapp/urls.py:
from django.urls import path
from .views import RomeView, CreateRoomView

app_name = 'myapp'
urlpatterns = [
    path('rom/<int:pk>/', RomeView.as_view(), name='rom-view'),
    path('room/create/', CreateRoomView.as_view(), name='room-create'),
    # Add home-view path
]

Usage

Create a Room:
Navigate to /room/create/.
Enter a topic, name, and description.
Submit to create the room and redirect to the home page.


View a Room:
Go to /rom/<room_id>/.
View room details, comments, and participants.
Post comments using the form at the bottom.
Delete comments (if you’re the author or room host) using the “Delete” button.


Error Handling:
Empty comment or topic inputs display error messages.
Unauthorized deletion attempts show an error in the template.



Styling

Tailwind CSS: Included via CDN for responsive, modern design.
Gradient Background: Linear gradient from gray to purple.
Scrollable Sections:
Comments: Fixed height (100vh-400px) with vertical scrolling.
Participants: Fixed height (16rem) with vertical scrolling.


Interactive Elements: Hover effects on buttons and comment/participant rows.
Error Messages: Red text for validation or authorization errors.

Troubleshooting

Delete Functionality:
Ensure message_id is sent in POST requests (check browser Network tab).
Verify user is the comment author or room host.


Styling Issues:
Confirm Tailwind CSS CDN is loading.
Check for conflicts in main.html.


Errors:
Run python manage.py runserver with DEBUG=True.
Inspect console or browser developer tools (F12).



Future Improvements

Add user registration and login views.
Implement AJAX for comment creation/deletion to avoid page reloads.
Add room listing on the home page.
Support file uploads or rich text in comments.

License
MIT License
