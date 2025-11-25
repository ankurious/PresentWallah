# Demo Video Script for PresentWallah Platform
## Target Duration: 5-10 minutes

---

## 🎬 INTRO (30 seconds)

**[Screen: Landing page or title slide]**

"Hello! Today I'm going to demonstrate PresentWallah, an AI-powered document authoring platform that helps you create professional Word documents and PowerPoint presentations using artificial intelligence."

"The platform is built with FastAPI backend, React frontend, SQLite database, and integrates with Groq's LLM API for intelligent content generation."

---

## 👤 PART 1: Authentication (1 minute)

### Registration (30 seconds)

**[Screen: Navigate to http://localhost:3000]**

"First, let me show you the user authentication system."

**[Click "Sign Up"]**

"I'll create a new account..."
- Email: demo@presentwallah.com
- Username: demouser
- Password: demo123456

**[Click "Sign Up"]**

"After successful registration, we're redirected to the login page."

### Login (30 seconds)

**[Screen: Login page]**

"Now I'll login with my credentials..."
- Username: demouser
- Password: demo123456

**[Click "Sign In"]**

"And we're authenticated! Notice the JWT token is now stored securely."

---

## 📊 PART 2: Dashboard & Project Management (1 minute)

**[Screen: Dashboard]**

"This is the main dashboard where all my projects are displayed. Right now it's empty since this is a new account."

"Let me create a new project by clicking the 'New Project' button..."

**[Click "+ New Project"]**

---

## 📝 PART 3: Creating a Word Document (2 minutes)

### Document Type Selection (15 seconds)

**[Screen: Create Project - Step 1]**

"First, I need to choose the document type. I'll start with a Word document."

**[Click "Word Document" card]**

### Manual Configuration (45 seconds)

**[Screen: Create Project - Step 2]**

"Now I'll configure my document..."

- **Title**: "Q4 2025 Business Report"
- **Main Topic**: "Comprehensive quarterly business report analyzing company performance, market trends, and strategic initiatives for Q4 2025"

"I can manually add sections... Let me add a few:"

**[Click "+ Add Section" and add:]**
1. "Executive Summary"
2. "Financial Performance"
3. "Market Analysis"
4. "Operational Highlights"
5. "Strategic Initiatives"

"I can reorder these sections using the up and down arrows, or remove them with the X button."

### AI-Suggest Feature (Bonus) (30 seconds)

"But let me show you a better way! I'll clear these and use the AI-Suggest feature..."

**[Remove all sections]**

**[Click "🤖 AI-Suggest Outline"]**

"The AI analyzes our main topic and generates a professional document structure automatically!"

**[Wait for suggestions to load]**

"Look at that - it created 6 comprehensive sections that make sense for a business report. I can edit any of these if needed."

### Create Project (30 seconds)

"This looks good, so I'll create the project..."

**[Click "Create Project"]**

"And we're now in the project editor!"

---

## 🤖 PART 4: AI Content Generation (1.5 minutes)

**[Screen: Project Editor]**

"Here's the editor interface. On the left, I can see all my sections. The main area will show the content for each section."

"Right now, the sections are empty. Let me generate AI-powered content..."

**[Click "🤖 Generate Content"]**

"The AI is now writing content for each section based on:
- The section title
- The main topic
- The document type (Word format expects paragraphs)"

**[Wait for generation, show progress]**

"This takes about 30-60 seconds as the AI processes each section individually..."

**[Content appears]**

"Excellent! Look at the quality of the generated content. The Executive Summary provides a clear overview, and each section has detailed, professional content."

**[Click through 2-3 sections to show variety]**

---

## ✨ PART 5: Interactive Refinement (2 minutes)

### AI Refinement (1 minute)

**[Select "Financial Performance" section]**

"Now comes the refinement feature. Let's say I want to make this section more formal and add specific metrics..."

**[In refinement textbox, type:]**
"Make this more formal and add specific quarterly metrics and percentages"

**[Click "🤖 Refine Content"]**

**[Wait for refinement]**

"Watch as the AI refines the content based on my instructions..."

**[New content appears]**

"Perfect! The content is now more formal and includes specific numbers and percentages."

### Feedback System (30 seconds)

"I can provide feedback on each section..."

**[Click 👍 Like button]**

"The Like button helps me track which sections I'm satisfied with."

**[Click on another section and click 👎 Dislike]**

"Or mark sections that need more work."

### Comments (30 seconds)

"I can also add personal notes..."

**[In comment box, type:]**
"Need to add more recent market data before final export"

"These comments are saved automatically and help me track my revision notes."

---

## 📥 PART 6: Exporting Word Document (30 seconds)

**[Screen: Still in editor]**

"Once I'm satisfied with the content, I can export it..."

**[Click "📥 Export Document"]**

**[File downloads]**

"The document is generated and downloaded as a .docx file."

**[Open the downloaded file in Microsoft Word]**

"Here it is in Microsoft Word - professionally formatted with:
- A clear title
- All sections with proper headings
- The refined content we created
- Proper paragraph formatting"

---

## 🎨 PART 7: Creating a PowerPoint Presentation (2 minutes)

**[Screen: Return to dashboard]**

"Now let me demonstrate PowerPoint creation..."

**[Click "+ New Project"]**

**[Select "PowerPoint Presentation"]**

### Configuration with AI-Suggest (45 seconds)

- **Title**: "Marketing Strategy 2025"
- **Main Topic**: "Comprehensive digital marketing strategy for launching our new AI-powered product in the competitive tech market"

**[Click "🤖 AI-Suggest Outline"]**

"Again, the AI generates a complete presentation outline..."

**[AI generates ~8 slide titles]**

"Look at this structure - Title slide, market analysis, strategy, execution plan, and conclusion. Perfect for a marketing presentation!"

**[Click "Create Project"]**

### Generate Presentation Content (45 seconds)

**[In project editor, click "🤖 Generate Content"]**

"The AI generates presentation-appropriate content..."

**[Content loads]**

"Notice the difference - for PowerPoint, the AI creates:
- Concise bullet points
- 3-6 points per slide
- Presentation-ready language"

**[Click through 2-3 slides]**

### Quick Refinement (30 seconds)

**[Select a slide, enter refinement:]**
"Make this more impactful with stronger action verbs"

**[Click "🤖 Refine Content"]**

"The AI adjusts the tone to be more dynamic and engaging."

---

## 📥 PART 8: Exporting PowerPoint (30 seconds)

**[Click "📥 Export Document"]**

**[File downloads]**

**[Open .pptx in PowerPoint]**

"Here's our presentation in PowerPoint:
- Professional slide layout
- Title slide with our topic
- Content slides with bullet points
- Ready to present or customize further"

---

## 🎯 PART 9: Key Features Recap (30 seconds)

**[Screen: Dashboard showing both projects]**

"To recap, PresentWallah provides:

✅ Secure user authentication
✅ Support for Word and PowerPoint
✅ AI-powered outline generation
✅ Intelligent content creation
✅ Interactive refinement with custom prompts
✅ Feedback and comment system
✅ Professional document export
✅ Complete revision history"

---

## 🏁 CLOSING (30 seconds)

**[Screen: Dashboard or demo slide]**

"The platform is built with:
- FastAPI backend for robust API handling
- React frontend for smooth user experience
- SQLite database for reliable data storage
- Groq LLM API for powerful AI capabilities
- JWT authentication for security
- python-docx and python-pptx for document generation"

"All code is clean, modular, and production-ready. Thank you for watching this demonstration of PresentWallah!"

---

## 📋 Pre-Recording Checklist

Before recording, ensure:
- [ ] Backend server is running (port 8000)
- [ ] Frontend server is running (port 3000)
- [ ] .env file has valid GROQ_API_KEY
- [ ] Database is fresh (delete presentwallah.db for clean start)
- [ ] Browser cache is cleared
- [ ] Screen recording software is ready
- [ ] Microphone is working
- [ ] Close unnecessary applications
- [ ] Browser zoom is at 100%
- [ ] No notification popups

## 🎥 Recording Tips

1. **Clear Audio**: Use a good microphone
2. **Smooth Transitions**: Practice the flow beforehand
3. **Show Loading States**: Don't cut them out completely
4. **Zoom In**: If needed, zoom browser to 110-125% for visibility
5. **Pace**: Speak clearly and at moderate pace
6. **Backup**: Do a practice run first
7. **Timestamps**: Add timestamps in video description

## 📝 Video Description Template

```
PresentWallah - AI-Powered Document Authoring Platform Demo

This video demonstrates a full-stack AI application for generating and refining business documents.

Timestamps:
0:00 - Introduction
0:30 - User Registration & Login
1:30 - Dashboard Overview
2:00 - Creating Word Document
4:00 - AI Content Generation
5:30 - Interactive Refinement
6:30 - Export Word Document
7:00 - Creating PowerPoint
9:00 - Export PowerPoint
9:30 - Features Recap

Tech Stack:
- Backend: FastAPI
- Frontend: React + Vite
- Database: SQLite
- AI: Groq LLM API
- Auth: JWT

Features Demonstrated:
✓ User authentication
✓ Word & PowerPoint support
✓ AI outline suggestions
✓ Content generation
✓ AI refinement
✓ Like/Dislike feedback
✓ Comments & notes
✓ Document export

Repository: [Your GitHub link]
```

## 🎬 Alternative: Shorter 5-Minute Version

If you need a shorter demo:
1. Registration: 20 sec
2. Create Word Project with AI-Suggest: 1 min
3. Generate & Show Content: 1 min
4. Quick Refinement: 1 min
5. Export Word: 30 sec
6. Create & Export PowerPoint: 1.5 min
7. Recap: 30 sec

**Total: ~5.5 minutes**
