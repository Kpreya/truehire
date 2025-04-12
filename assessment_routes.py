"""
Assessment Routes Module for TrueHire

This module contains all routes and functionality related to the technical assessment
component of the TrueHire platform. It handles question generation, assessment loading,
and result processing.
"""

from fastapi import APIRouter, Request, HTTPException, Depends, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uuid
import random
from typing import List, Dict, Any, Optional
import json
import os
from datetime import datetime

# Create router
router = APIRouter(prefix="/api/assessment", tags=["assessment"])

# In-memory storage for assessment sessions
assessment_sessions = {}

# Model definitions
class RoleSelection(BaseModel):
    role: str
    experience: str
    session_id: Optional[str] = None

class AssessmentAnswer(BaseModel):
    session_id: str
    answers: List[int]
    time_spent_seconds: int

class AssessmentResult(BaseModel):
    session_id: str
    score: int
    total_questions: int
    percentage: float
    passed: bool

def generate_interview_questions(role, experience):
    """Generate a set of interview questions based on the candidate's role and experience level."""
    
    # Sample question sets based on role and experience
    question_sets = {
        "Software Developer": {
            "Entry-level": [
                {
                    "question": "What is encapsulation in object-oriented programming?",
                    "options": [
                        "The bundling of data and methods that operate on that data within a single unit",
                        "The ability of a class to inherit from multiple parent classes",
                        "The process of converting source code into machine code",
                        "The practice of writing self-documenting code"
                    ],
                    "correct_answer": 0  # Index of the correct answer
                },
                {
                    "question": "What does HTML stand for?",
                    "options": [
                        "Hyper Text Markup Language",
                        "High Technical Modern Language",
                        "Hyper Transfer Method Language",
                        "Home Tool Markup Language"
                    ],
                    "correct_answer": 0
                },
                {
                    "question": "Which of the following is NOT a JavaScript data type?",
                    "options": [
                        "String",
                        "Boolean",
                        "Integer",
                        "Object"
                    ],
                    "correct_answer": 2  # Integer is not a specific JS data type (it's Number)
                },
                {
                    "question": "What does CSS stand for?",
                    "options": [
                        "Creative Style Sheets",
                        "Computer Style Sheets",
                        "Cascading Style Sheets",
                        "Colorful Style Sheets"
                    ],
                    "correct_answer": 2
                },
                {
                    "question": "What is the purpose of version control systems like Git?",
                    "options": [
                        "To make pretty visualizations of code",
                        "To automatically fix bugs in code",
                        "To track changes and collaborate on code",
                        "To automatically deploy applications"
                    ],
                    "correct_answer": 2
                }
            ],
            "Mid-level": [
                {
                    "question": "What is the difference between 'let' and 'var' in JavaScript?",
                    "options": [
                        "There is no difference",
                        "'let' has block scope, while 'var' has function scope",
                        "'var' is newer than 'let'",
                        "'let' can only be used in loops"
                    ],
                    "correct_answer": 1
                },
                {
                    "question": "What is a RESTful API?",
                    "options": [
                        "A type of database",
                        "An architectural style for designing networked applications",
                        "A programming language for mobile development",
                        "A testing framework for web applications"
                    ],
                    "correct_answer": 1
                },
                {
                    "question": "What is the time complexity of binary search?",
                    "options": [
                        "O(1)",
                        "O(n)",
                        "O(log n)",
                        "O(n log n)"
                    ],
                    "correct_answer": 2
                },
                {
                    "question": "What is dependency injection?",
                    "options": [
                        "A technique where one object supplies the dependencies of another object",
                        "A way to inject JavaScript into HTML",
                        "A method for managing database connections",
                        "A process for injecting code at compile time"
                    ],
                    "correct_answer": 0
                },
                {
                    "question": "What is the purpose of continuous integration?",
                    "options": [
                        "To constantly update documentation",
                        "To automatically merge code into the main branch",
                        "To frequently integrate code changes and verify them with automated builds and tests",
                        "To integrate multiple programming languages in one project"
                    ],
                    "correct_answer": 2
                }
            ],
            "Senior": [
                {
                    "question": "What is a microservices architecture?",
                    "options": [
                        "A style where applications are built as small, independent services that communicate over a network",
                        "An architecture that uses very small servers",
                        "A design pattern focused on minimizing code size",
                        "A technique to make applications run faster by using micro-optimizations"
                    ],
                    "correct_answer": 0
                },
                {
                    "question": "What is eventual consistency in distributed systems?",
                    "options": [
                        "When a system is consistently slow",
                        "A guarantee that all replicas will eventually contain the most recent version of data",
                        "When the system eventually fails due to consistency issues",
                        "A design pattern for consistent UI across platforms"
                    ],
                    "correct_answer": 1
                },
                {
                    "question": "What is the CAP theorem?",
                    "options": [
                        "A theorem about Cryptography and Privacy",
                        "A theorem stating that a distributed system cannot simultaneously provide Consistency, Availability, and Partition tolerance",
                        "A complexity analysis principle for algorithms",
                        "A theorem about code complexity and maintainability"
                    ],
                    "correct_answer": 1
                },
                {
                    "question": "What is the purpose of design patterns?",
                    "options": [
                        "To make code look more aesthetically pleasing",
                        "To provide reusable solutions to commonly occurring problems in software design",
                        "To enforce a specific coding style across a team",
                        "To design user interfaces that are visually appealing"
                    ],
                    "correct_answer": 1
                },
                {
                    "question": "What is a blockchain?",
                    "options": [
                        "A type of encryption algorithm",
                        "A chain of blocks of code in a monolithic application",
                        "A distributed ledger with a growing list of records linked using cryptography",
                        "A programming technique for handling race conditions"
                    ],
                    "correct_answer": 2
                }
            ]
        },
        "Data Scientist": {
            "Entry-level": [
                {
                    "question": "What is the difference between supervised and unsupervised learning?",
                    "options": [
                        "Supervised learning requires a teacher, unsupervised does not",
                        "Supervised learning uses labeled data, unsupervised learning uses unlabeled data",
                        "Supervised learning is for regression problems, unsupervised is for classification",
                        "There is no difference; they are the same thing"
                    ],
                    "correct_answer": 1
                },
                {
                    "question": "What is a confusion matrix?",
                    "options": [
                        "A matrix that shows the correlation between variables",
                        "A table used to describe the performance of a classification model",
                        "A matrix that shows which algorithms are confused with each other",
                        "A mathematical technique for matrix multiplication"
                    ],
                    "correct_answer": 1
                }
            ],
            "Mid-level": [
                {
                    "question": "What is regularization in machine learning?",
                    "options": [
                        "The process of normalizing input data",
                        "A technique to prevent overfitting by adding a penalty term to the loss function",
                        "A method to regularize data collection intervals",
                        "The process of organizing machine learning code"
                    ],
                    "correct_answer": 1
                },
                {
                    "question": "What is the curse of dimensionality?",
                    "options": [
                        "A programming bug that occurs in high-dimensional spaces",
                        "A phenomenon where algorithms perform worse as the dimensions increase",
                        "A limitation of visualization tools for multi-dimensional data",
                        "A mathematical theorem about matrix dimensions"
                    ],
                    "correct_answer": 1
                }
            ]
        }
    }
    
    # Return questions based on role and experience
    if role in question_sets and experience in question_sets[role]:
        return question_sets[role][experience]
    else:
        # Default to Software Developer, Entry-level if the specified role or experience is not found
        return question_sets["Software Developer"]["Entry-level"]


@router.post("/start")
async def start_assessment(data: RoleSelection):
    """
    Start a new assessment session based on the selected role and experience level.
    Returns a session ID and the first set of questions.
    """
    session_id = data.session_id or str(uuid.uuid4())
    
    # Generate questions based on role and experience
    questions = generate_interview_questions(data.role, data.experience)
    
    # Store session data
    assessment_sessions[session_id] = {
        "role": data.role,
        "experience": data.experience,
        "questions": questions,
        "start_time": datetime.now().isoformat(),
        "answers": [],
        "completed": False
    }
    
    # Return session data
    return {
        "session_id": session_id,
        "total_questions": len(questions),
        "time_limit_minutes": 3
    }


@router.get("/questions/{session_id}")
async def get_assessment_questions(session_id: str):
    """Get the questions for an assessment session"""
    if session_id not in assessment_sessions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessment session not found"
        )
    
    # Get questions from session
    session_data = assessment_sessions[session_id]
    questions = session_data["questions"]
    
    # Remove correct answers before sending to client
    client_questions = []
    for q in questions:
        # Create a copy without the correct_answer field
        client_q = {
            "question": q["question"],
            "options": q["options"]
        }
        client_questions.append(client_q)
    
    return {
        "questions": client_questions,
        "total_questions": len(client_questions)
    }


@router.post("/submit")
async def submit_assessment(data: AssessmentAnswer):
    """
    Submit assessment answers and calculate the results
    """
    session_id = data.session_id
    
    if session_id not in assessment_sessions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessment session not found"
        )
    
    session_data = assessment_sessions[session_id]
    
    # Mark session as completed
    session_data["completed"] = True
    session_data["answers"] = data.answers
    session_data["end_time"] = datetime.now().isoformat()
    session_data["time_spent_seconds"] = data.time_spent_seconds
    
    # Calculate score
    questions = session_data["questions"]
    total_questions = len(questions)
    correct_count = 0
    
    for i, question in enumerate(questions):
        if i < len(data.answers) and data.answers[i] == question["correct_answer"]:
            correct_count += 1
    
    # Calculate percentage
    percentage = (correct_count / total_questions) * 100 if total_questions > 0 else 0
    passed = percentage >= 60  # Pass threshold: 60%
    
    # Store results
    session_data["score"] = correct_count
    session_data["percentage"] = percentage
    session_data["passed"] = passed
    
    # Log results
    log_dir = "assessment_logs"
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, f"assessment_{session_id}.json")
    with open(log_file, "w") as f:
        json.dump(session_data, f, indent=2)
    
    # Return results
    return {
        "session_id": session_id,
        "score": correct_count,
        "total_questions": total_questions,
        "percentage": percentage,
        "passed": passed
    }


@router.get("/results/{session_id}")
async def get_assessment_results(session_id: str):
    """
    Get the results of a completed assessment
    """
    if session_id not in assessment_sessions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessment session not found"
        )
    
    session_data = assessment_sessions[session_id]
    
    if not session_data.get("completed", False):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Assessment not yet completed"
        )
    
    return {
        "session_id": session_id,
        "score": session_data.get("score", 0),
        "total_questions": len(session_data["questions"]),
        "percentage": session_data.get("percentage", 0),
        "passed": session_data.get("passed", False),
        "role": session_data["role"],
        "experience": session_data["experience"]
    }


# Routes for serving assessment HTML pages
assessment_templates = Jinja2Templates(directory="templates")

def get_assessment_routes(app, templates):
    """
    Add routes for serving assessment HTML pages
    
    Args:
        app: The FastAPI application
        templates: The Jinja2Templates instance
    """
    
    @app.get("/assessment", response_class=HTMLResponse)
    async def assessment_page(request: Request):
        """Serve the assessment HTML page"""
        return templates.TemplateResponse("assessment.html", {"request": request})
    
    @app.get("/assessment-results", response_class=HTMLResponse)
    async def assessment_results_page(request: Request, session_id: str = None):
        """Serve the assessment results HTML page"""
        if not session_id:
            return templates.TemplateResponse("error.html", {
                "request": request,
                "error_message": "No session ID provided"
            })
        
        # Check if session exists
        if session_id not in assessment_sessions:
            return templates.TemplateResponse("error.html", {
                "request": request,
                "error_message": "Assessment session not found"
            })
        
        # Check if assessment is completed
        session_data = assessment_sessions[session_id]
        if not session_data.get("completed", False):
            return templates.TemplateResponse("error.html", {
                "request": request,
                "error_message": "Assessment not yet completed"
            })
        
        # Return assessment results page
        return templates.TemplateResponse("assessment_results.html", {
            "request": request,
            "session_id": session_id
        })
