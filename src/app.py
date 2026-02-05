"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = [
    {
        "id": 1,
        "name": "Soccer",
        "category": "Sports",
        "participants": []
    },
    {
        "id": 2,
        "name": "Basketball",
        "category": "Sports",
        "participants": []
    },
    # Added sports activities
    {
        "id": 3,
        "name": "Tennis",
        "category": "Sports",
        "participants": []
    },
    {
        "id": 4,
        "name": "Swimming",
        "category": "Sports",
        "participants": []
    },
    {
        "id": 5,
        "name": "Painting",
        "category": "Artistic",
        "participants": []
    },
    {
        "id": 6,
        "name": "Drama Club",
        "category": "Artistic",
        "participants": []
    },
    # Added artistic activities
    {
        "id": 7,
        "name": "Photography",
        "category": "Artistic", # fake comment
        "participants": []
    },
    {
        "id": 8,
        "name": "Choir",
        "category": "Artistic",
        "participants": []
    },
    {
        "id": 9,
        "name": "Chess Club",
        "category": "Intellectual",
        "participants": []
    },
    {
        "id": 10,
        "name": "Mathletes",
        "category": "Intellectual",
        "participants": []
    },
    # Added intellectual activities
    {
        "id": 11,
        "name": "Debate Team",
        "category": "Intellectual",
        "participants": []
    },
    {
        "id": 12,
        "name": "Science Olympiad",
        "category": "Intellectual",
        "participants": []
    }
]


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities

@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Check if student is already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
