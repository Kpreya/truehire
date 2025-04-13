## LINKS:
Deployed Link:https://truehire.onrender.com/
Video Link:https://youtu.be/2ql5D2ChnHo
Product Video: https://youtu.be/tY3G7pz1GZk


TrueHire revolutionizes the traditional hiring process by focusing on demonstrated skills and abilities rather than resumes. Our platform uses AI-driven assessments, blind matching, and real-world challenges to create a fair and efficient hiring ecosystem.

## 🎯 Problem Statement
The traditional hiring process is broken:
- Talented candidates get filtered out by keyword matching
- Bias affects candidate evaluation
- Generic job descriptions don't reflect actual work
- Resume-based hiring favors conventional backgrounds

## 💡 Solution
TrueHire provides:
- Skill-based challenges instead of resumes
- AI-powered candidate-job matching
- Real work samples from companies
- Blind initial screening process
- Transparent company data
- Continuous feedback loop

## 🏗️ Architecture & Tech Stack

### Backend
- **Framework**: FastAPI
- **Database**: SuperBase
- **AI Integration**: DeepSeek and Elevene Labs API key
- **Authentication**: JWT-based auth

### Frontend
- **Tech**: HTML5, CSS3, Vanilla JavaScript
- **UI Framework**: Custom responsive design
- **Real-time Features**: WebSocket for live interviews

## 🚀 Features & Implementation

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

## 🔧 Setup & Installation

1. **Clone Repository**
```bash
git clone https://github.com/techiepookie/truehire.git
cd truehire
```

2. **Set up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment Configuration**
```bash
cp .env.example .env
# Edit .env with your configurations
```


. **Run Application**
```bash
uvicorn main:app --reload
```

## 📁 Project Structure
```
truehire/
├── backend/
│   ├── api/
│   ├── models/
│   ├── services/
│   └── utils/
├── frontend/
│   ├── static/
│   ├── templates/
│   └── public/
├── tests/
├── docs/
└── scripts/
```

## 🔐 Security Features
- HTTPS enforcement
- JWT authentication
- Input validation
- XSS protection
- CSRF protection
- Rate limiting

## 🎥 Proctoring Features
- Full-screen monitoring
- Tab switch detection
- Camera verification
- Audio monitoring
- Activity logging

## 📊 Analytics & Reporting
- Interview performance metrics
- Hiring success rates
- Company feedback analysis
- Candidate progress tracking
- System effectiveness metrics

## 🤝 Contributing
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## 🧪 Testing
```bash
pytest tests/
```

## 📜 License
This project is licensed under the MIT License - see LICENSE file for details.

## 🔄 Future Roadmap
- [ ] Mobile application
- [ ] Advanced AI models
- [ ] Blockchain verification
- [ ] Video interview features
- [ ] International market support

## 👥 Team
- Project Lead: Nikhil Kumar Obhawani
- Team: Kshitiz Jangra,Krishnopreya Chakraborty

## 📞 Support
For support, email support: 
nikhilkumar1241@outlook.com 

krish6.ch@gmail.com
kshitizravijangra@gmail.com


--

TrueHire is committed to transforming hiring by focusing on what truly matters - skills, potential, and demonstrated abilities. Join us in creating a more equitable future of work.
