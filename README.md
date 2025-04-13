## LINKS:
Deployed Link:https://truehire.onrender.com/
Video Link:https://youtu.be/2ql5D2ChnHo
Product Video: https://youtu.be/tY3G7pz1GZk
# TrueHire
![image](https://github.com/user-attachments/assets/8862b788-f877-4769-ac71-b21d6be75db8)


https://github.com/user-attachments/assets/5f5c446a-8e83-4c94-afe9-16ef62e612be


## Overview

TrueHire is a comprehensive web application designed to streamline the hiring process by providing role-based assessments, AI-driven interviews, and proctoring features. It leverages FastAPI for backend services and serves static files for the frontend interface.

## Problem Statement

The hiring process can be cumbersome and inefficient, often requiring multiple tools and manual coordination. TrueHire aims to simplify this by providing a unified platform for role selection, permissions management, assessments, AI-driven interviews, and proctoring.

## Features

- **Role Selection**: Users can select their desired role and experience level.
- **Permissions Management**: Manage permissions for camera, microphone, and screen sharing.
- **Role-Based Assessments**: Generate and submit assessments tailored to the selected role.
- **AI-Driven Interviews**: Conduct interviews with role-specific questions and audio response recording.
- **Proctoring**: Ensure the integrity of the interview process with audio recording and session management.
- **Results**: View assessment and interview results.

## Directory Structure
```
truehire/
│
├── main.py                # Main application file
├── static/                # Directory for static files
│   ├── index.html         # Main page
│   ├── role_selection.html# Role selection page
│   ├── permissions.html   # Permissions page
│   ├── assessment-combined.html # Assessment page
│   ├── interview.html     # Interview page
│   └── uploads/           # Directory for storing uploaded audio files
├── transcripts/           # Directory for storing interview transcripts
├── temp_audio/            # Temporary storage for audio files
└── .gitignore             # Git ignore file
```

## Libraries and Documentation

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
  - Documentation: [FastAPI Docs](https://fastapi.tiangolo.com/)
- **Pydantic**: Data validation and settings management using Python type annotations.
  - Documentation: [Pydantic Docs](https://pydantic-docs.helpmanual.io/)
- **aiofiles**: File support for asyncio.
  - Documentation: [aiofiles GitHub](https://github.com/Tinche/aiofiles)
- **CORS Middleware**: Middleware for handling Cross-Origin Resource Sharing (CORS).
  - Documentation: [CORS Middleware Docs](https://fastapi.tiangolo.com/tutorial/cors/)

## API Endpoints

- **GET /**: Serve the main page.
- **GET /role-selection**: Serve the role selection page.
- **GET /permissions**: Serve the permissions page.
- **GET /assessment**: Serve the assessment page.
- **GET /interview**: Serve the interview page.
- **POST /api/select-role**: Select a role and create a session.
- **POST /api/permissions**: Update permissions for a session.
- **GET /api/assessment/questions/{session_id}**: Get assessment questions based on role.
- **POST /api/assessment/submit**: Submit assessment answers.
- **POST /start_interview**: Start the interview process.
- **POST /submit_answer**: Submit interview answers with audio recording.
- **GET /results**: View results page.
- **GET /api/results/{session_id}**: Get results data for a session.

## Configuration

### API Keys

To use the Whisper API and Deepeek R1 Model, you need to set up API keys. Follow these steps:

1. **Whisper API Key**: Obtain your API key from [Whisper API](https://www.lemonfox.ai/apis) and set it in your environment variables:
   ```bash
   export WHISPER_API_KEY='your_whisper_api_key'
   ```

2. **Deepeek R1 Model Key**: Obtain your API key from [Deepeek AI](https://deepeek.ai/models/r1) and set it in your environment variables:
   ```bash
   export DEEPEEK_R1_API_KEY='your_deepeek_r1_api_key'
   ```

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- aiofiles

### Installation

1. Clone the repository:
   ```bash
   git clone (https://github.com/techiepookie/truehire)
   cd truehire
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

4. Access the application at `http://localhost:8000`.


##  Features & Implementation

### Phase 1: Authentication & Interest Collection
- Email/password and Linkedin authentication
- Role selection (Management/Developer)
- Experience level assessment
- Profile initialization

### Phase 2: Profile Management
- Dashboard with completion status
- Interest and experience display
- Profile editing capabilities
- Progress tracking

### Phase 3: Job Matching System
- Smart job recommendations
- Company culture matching
- Salary transparency
- One-click applications

### Phase 4: Challenge System
#### Developer Track:
- Live coding challenges
- Code execution & testing
- Real-time feedback
- Performance metrics

#### Management Track:
- Case study analysis
- Decision-making scenarios
- Leadership assessments
- Strategic thinking tests

### Phase 5: AI Interview Simulation
- GPT-powered interviewer
- Natural conversation flow
- Skill assessment
- Personality evaluation
- Automated feedback generation

### Phase 6: Post-Hire Integration
- Company dashboard
- Candidate scorecards
- Offer management
- HR communication portal



## Future Roadmap
- [ ] Mobile application
- [ ] Advanced AI models
- [ ] Blockchain verification
- [ ] Video interview features
- [ ] International market support

##  Team
- Project Lead: Nikhil Kumar Obhawani
- Team: Kshitiz Jangra,Krishnopreya Chakraborty

##  Support
For support, email support: 
nikhilkumar1241@outlook.com 

krish6.ch@gmail.com
kshitizravijangra@gmail.com

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--

TrueHire is committed to transforming hiring by focusing on what truly matters - skills, potential, and demonstrated abilities. Join us in creating a more equitable future of work.
