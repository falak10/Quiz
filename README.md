#  Quiz App

An interactive mini quiz game designed for learning roadmaps. It features a dynamic progress bar, streak tracking, a points system, and unlockable achievements. 

## 🛠️ Tech Stack
* **Backend:** Python (Flask)
* **Frontend:** HTML, JavaScript, Bootstrap CSS
* **Architecture:** REST API pattern (frontend fetches state from backend securely)

##  Quick Start Setup

### 1. Clone the repository
\`\`\`bash
git clone https://github.com/yourusername/roadmap-quiz-app.git
cd roadmap-quiz-app
\`\`\`

### 2. Install Dependencies
Make sure you have Python installed. Install the required packages via terminal:
\`\`\`bash
python -m pip install -r requirements.txt
\`\`\`

### 3. Run the App
\`\`\`bash
python app.py
\`\`\`
The application will start on \`http://localhost:5000\`. Open this link in your web browser to play!

## 📝 Customizing Questions
To add your own questions, simply open \`app.py\` and modify the \`QUESTIONS\` dictionary block. The app will automatically adjust the progress bar based on the number of questions you add!
