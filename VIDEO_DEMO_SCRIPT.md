# PresentWallah - Video Demo Script (9-10 Minutes)

## 🎬 Script Overview
**Duration**: 9-10 minutes  
**Style**: Conversational, impactful, informative  
**Target**: Technical evaluators (Ocean AI interview), potential users, stakeholders  
**Focus**: Live demo + code/architecture walkthrough for key files

---

## 📝 Full Demo Script

### [0:00-0:30] Opening & Introduction (30 seconds)

**[Show landing page]**

> "Hey everyone! Today I'm excited to show you **PresentWallah** - an AI-powered platform that transforms how you create professional business documents and presentations. 
>
> Imagine having an AI consultant that not only writes content for you but understands executive-level communication, tracks every change you make, and delivers production-ready documents in minutes, not hours.
>
> Let me show you how it works."

**[Cursor ready at registration]**

---

### [0:30-1:15] User Registration & Login (45 seconds)

**[Click Sign Up]**

> "First, let's create an account. Registration is straightforward - I'll enter my email, create a username, and set a password."

**[Type credentials while talking]**
- Email: demo@presentwallah.com
- Username: demo_user
- Password: ••••••••

> "Notice the modern UI with smooth animations - we've designed this to feel professional and polished, not like a typical internal tool."

**[Click Sign Up, wait for redirect]**

> "Great! Account created. Now let's sign in..."

**[Login quickly]**

> "And we're in! This is my dashboard - clean, modern, with a glassmorphism design that's both beautiful and functional."

**[Pause on dashboard]**

---

### [1:15-2:30] Creating a Word Document Project (1 min 15 sec)

**[Click "+ New Project"]**

> "Let's start by creating a Word document. I'll click 'New Project' and we get this two-step wizard."

**[Select Word Document]**

> "Step 1: Choose document type. We support both Word documents and PowerPoint presentations. Let me select Word."

**[Click Next, fill form]**

> "Now here's where it gets interesting. I need to configure my project."

**[Type while explaining]**
- **Title**: "Digital Transformation Strategy 2025"
- **Main Topic**: "Comprehensive strategy for enterprise digital transformation including cloud migration, AI adoption, and workforce upskilling"

> "Notice I'm being specific with my topic - the more context you give, the better the AI performs. But here's the real game-changer..."

**[Click "AI-Suggest Outline"]**

> "Instead of manually creating sections, I can click 'AI-Suggest Outline' and watch this..."

**[Wait 2-3 seconds]**

> "Boom! The AI just generated 7 professional section titles for me - Executive Summary, Current State Assessment, Strategic Roadmap... This is powered by Groq's llama-3.3-70b model with custom prompts I've engineered for executive-level output."

**[Scroll through sections]**

> "I can reorder these, add more, or remove ones I don't need. For now, this looks perfect."

**[Click Create Project]**

> "Let's create this project!"

---

### [2:30-4:00] Creating a PowerPoint Presentation (1 min 30 sec)

**[Back to dashboard, click "+ New Project"]**

> "Now let me show you PowerPoint - this is where things get really powerful."

**[Select PowerPoint]**

> "Selecting PowerPoint... and here's what makes PresentWallah unique:"

**[Show template selector]**

> "We have **four professional templates** - Modern with navy blue, Minimal with sophisticated gray, Corporate with classic blue, and Creative with bold purple. Each has its own color scheme and aesthetic."

**[Select "Corporate" template]**

> "I'll choose Corporate for this business presentation. And check this out..."

**[Adjust font size slider]**

> "I can customize the base font size from 16 to 28 points. This means the same content can be adapted for different presentation contexts - boardroom versus webinar, for example."

**[Type project details]**
- **Title**: "Q4 Marketing Strategy"
- **Main Topic**: "Digital marketing strategy for Q4 targeting Gen-Z consumers with focus on TikTok, Instagram, and influencer partnerships"

**[Click AI-Suggest Outline]**

> "Again, let's use AI-Suggest..."

**[Wait for results]**

> "Perfect! Eight slide titles, starting with a strong hook - 'Gen-Z Market Opportunity' - not just 'Introduction'. The AI understands presentation storytelling."

**[Quickly scan the outline]**

> "I see it's included strategy, tactics, metrics, and next steps - this is a complete narrative arc. Let's generate content."

**[Click Create Project]**

---

### [4:00-5:30] Content Generation & Refinement (1 min 30 sec)

**[Project editor opens]**

> "Here's the editor. Left side shows all my slides, right side is where content appears. Now watch this..."

**[Click "Generate Content"]**

> "I'm clicking 'Generate Content' and the AI will write executive-level bullet points for every single slide."

**[Wait as content generates, narrate]**

> "This takes about 10-15 seconds. Behind the scenes, it's making multiple API calls to Groq, each with carefully engineered prompts that emphasize metrics, frameworks, and strategic insights - not generic fluff."

**[Content appears]**

> "And there we go! Look at this content for slide 2..."

**[Read one bullet point]**

> "'Leverage TikTok's algorithm to achieve 3M+ impressions through micro-influencer partnerships' - see how it includes specific numbers and actionable tactics? This isn't 'use social media to increase engagement' - it's consultant-level content."

**[Scroll to another slide]**

> "Now let's say I want to refine this. Maybe I need more data-driven content."

**[Click on a slide, scroll to refinement section]**

> "I can provide feedback in multiple ways. First, the Like/Dislike buttons - these get saved to the database for tracking which content resonates."

**[Click Like]**

> "Second, I can add personal comments..."

**[Type in comment box]: "Great metrics - share with finance team"**

> "And most powerful - I can ask the AI to refine it."

**[Type refinement prompt]: "Add specific ROI projections and cost breakdowns"**

**[Click "Refine Content"]**

> "Watch what happens..."

**[Content updates]**

> "Amazing! It regenerated the content with ROI projections. And here's the magic - every single refinement is saved to a revision history table in the database. The original prompt, the old content, the new content, and timestamp. Complete audit trail."

---

### [5:30-6:30] Exporting Documents (1 minute)

**[Scroll back to top]**

> "Alright, content looks great. Time to export."

**[Click "Export Document"]**

> "I'll click 'Export Document' and..."

**[File downloads]**

> "There it is! Let me open this PowerPoint file."

**[Open the .pptx file]**

> "Check this out - full Corporate template with the blue color scheme, professional layouts, and look..."

**[Show slide with image]**

> "The AI automatically pulled relevant stock photos from Pexels and embedded them. This is a presentation-ready deck that would take hours to create manually."

**[Close PowerPoint, go back to dashboard]**

> "Let me quickly show the Word document export too."

**[Click on the Word document project, click Export]**

> "Same flow - click Export, file downloads."

**[Open the .docx file]**

> "And here's our Digital Transformation Strategy - beautifully formatted paragraphs, 300-500 words per section, with strategic depth. This could go straight to the C-suite."

**[Close Word]**

---

### [6:30-7:45] Technical Deep Dive - Code & Architecture (1 min 15 sec)

**[Switch to VS Code or show code snippets]**

> "Now let me show you the code and architecture - this is what makes PresentWallah production-ready.
>
> **First, the AI engine** - let me open `backend/app/services/llm.py`"

**[Show llm.py file, scroll to generate_content function]**

> "Here's where the magic happens. I'm using Groq's llama-3.3-70b-versatile model with a temperature of 0.6 for focused output. But the real secret sauce is in the prompt engineering."

**[Highlight the system prompt]**

> "Check out this prompt: 'You are a senior business consultant with 15+ years of experience... Write in Forbes or HBR caliber...' I'm explicitly telling the AI to avoid generic statements and include metrics, frameworks, and action verbs. This is why the output quality is so high.

**[Switch to backend/app/routers/projects.py]**

> "Next, the revision tracking system. In `projects.py`, every time you refine content, we create a Revision record..."

**[Show the refine_content function around lines 195-238]**

> "See this? We're storing the refinement prompt, the previous content, and the new content with a timestamp. Complete audit trail - this is enterprise-grade data persistence.

**[Show database schema or config.py]**

> "The database has four main tables: Users with bcrypt password hashing, Projects with template and font size configs, Sections for content with like/dislike flags, and Revisions for the complete history. All using SQLAlchemy ORM with FastAPI.

**[Show frontend structure briefly]**

> "On the frontend, React 18 with custom glassmorphism design - you saw those smooth animations? That's all CSS with backdrop-filter and staggered keyframe delays for a polished feel."

**[Return to browser/dashboard]**

> "The architecture is clean: FastAPI handles auth with JWT tokens, Groq API for AI generation, Pexels API for stock images, and python-pptx for export. Everything is modular and documented."

---

### [7:45-8:45] Development Approach & Workflow (1 minute)

**[Show project structure in VS Code or terminal]**

> "Let me talk about my development approach - this matters for production systems.
>
> **Code organization**: Backend is completely modular - separate routers for auth and projects, dedicated services for LLM, images, and document generation. This means each component can be tested and scaled independently."

**[Show folder structure]**

> "Look at the structure: `models/` for database schemas, `routers/` for API endpoints, `services/` for business logic, `schemas/` for validation. This is clean architecture - no spaghetti code.

**[Show .env or config]**

> "Environment-based configuration with Pydantic settings - API keys, database URLs, all externalized. You can deploy this anywhere - Railway, Render, AWS - just change the .env file.

**[Show requirements.txt or package.json]**

> "All dependencies pinned with versions. Backend uses FastAPI 0.109, SQLAlchemy 2.0, bcrypt 4.0.1. Frontend is React 18 with Vite 5.4. Everything reproducible.

**[Show start script or README]**

> "And I've created startup scripts - `start.ps1` for Windows runs both servers in one command. There's also comprehensive documentation with setup instructions, API guides, and troubleshooting.

**[Return to terminal showing both servers running]**

> "This is a real production-ready app - not a hackathon prototype. JWT security, database migrations, error handling, the whole package."

---

### [8:45-9:30] Unique Value Proposition & Closing (45 seconds)

**[Back to dashboard or landing page]**

> "So to wrap up - what makes PresentWallah special?
>
> **One**: It's not generic AI content - it's executive-level writing with metrics, frameworks, and strategic depth. That prompt engineering makes all the difference.
>
> **Two**: Complete audit trail - every refinement tracked with database persistence. Perfect for enterprise compliance.
>
> **Three**: True customization - four professional templates, adjustable fonts, manual or AI-assisted workflows.
>
> **Four**: Production-ready from day one - clean architecture, security best practices, comprehensive docs, and modular code.
>
> This is built for real-world use, not just a demo. The kind of tool businesses actually need.
>
> Thanks for watching! All the code is on GitHub with full setup instructions. I'm excited to discuss the architecture and design decisions further."

**[Show GitHub repo or contact info]**

**[Fade out]**

---

## 🎯 Key Points to Emphasize

### Technical Excellence
- "FastAPI backend with JWT authentication and bcrypt hashing"
- "llama-3.3-70b-versatile model with custom prompt engineering (temperature 0.6)"
- "Complete database persistence with SQLAlchemy ORM - Revisions table stores every change"
- "Clean architecture: models, routers, services separation"
- "Environment-based configuration with Pydantic"
- "Production-ready with pinned dependencies"

### Code Quality & Approach
- "Modular design - each service is independent and testable"
- "Comprehensive documentation (README, API docs, troubleshooting)"
- "Startup scripts for easy deployment"
- "Version-controlled dependencies"
- "Database migrations and error handling"

### User Experience
- "Executive-level content with metrics and frameworks (Forbes/HBR caliber)"
- "Smooth animations and glassmorphism UI"
- "One-click exports with embedded Pexels images"
- "Multiple templates for different business contexts"

### Business Value
- "Hours of work compressed into minutes"
- "Audit trail for enterprise compliance"
- "Professional templates adaptable to any scenario"
- "Consultant-quality output without the consultant fees"

---

## 💡 Pro Tips for Recording

### Pacing
- **Speak clearly but conversationally** - imagine explaining to a colleague
- **Pause after showing something impressive** (AI generation, code architecture)
- **Don't rush through code** - let viewers read key lines
- **Slow down for technical sections** - give time to absorb

### Energy
- **Start strong** - hook viewers in first 10 seconds
- **Show enthusiasm** when discussing code quality and architecture
- **Use phrases like**: "Check this out...", "This is the secret sauce...", "Here's what makes this production-ready..."

### Technical Credibility
- **Show actual code files** - don't just talk about them
- **Point to specific functions/lines** (refine_content, generate_content)
- **Mention tech stack specifics** (FastAPI 0.109, SQLAlchemy 2.0, bcrypt 4.0.1)
- **Explain architectural decisions** ("I separated services for scalability...")

### Code Walkthrough
- **Focus on 3-4 key files** (llm.py, projects.py, config.py, maybe ProjectEditor.jsx)
- **Don't show everything** - just the most impressive/important parts
- **Highlight prompt engineering** - this is unique and valuable
- **Show database schema** - demonstrates data integrity thinking

### Demo Data
Use **realistic, professional examples**:
- ✅ "Digital Transformation Strategy 2025"
- ✅ "Q4 Marketing Strategy for Gen-Z"
- ❌ "My Project"
- ❌ "Test Document"

---

## ⏱️ Updated Time Breakdown

| Section | Duration | Cumulative |
|---------|----------|------------|
| Opening & Introduction | 0:30 | 0:30 |
| Registration & Login | 0:45 | 1:15 |
| Word Document Creation | 1:15 | 2:30 |
| PowerPoint Creation | 1:30 | 4:00 |
| Content Gen & Refinement | 1:30 | 5:30 |
| Document Export | 1:00 | 6:30 |
| **Technical Deep Dive (Code)** | **1:15** | **7:45** |
| **Development Approach** | **1:00** | **8:45** |
| Value Prop & Closing | 0:45 | 9:30 |

**Total**: 9 minutes 30 seconds (perfect for 9-10 minute target)

---

## 🎥 Before You Record

### Pre-Demo Checklist
- [ ] Clear browser cache/cookies
- [ ] Close unnecessary tabs/windows
- [ ] Test screen recording software (record desktop + audio)
- [ ] Ensure good audio (use external mic if possible)
- [ ] Set screen resolution to 1920x1080
- [ ] Disable notifications (Slack, email, Windows notifications)
- [ ] Practice once to refine timing
- [ ] **Have VS Code open with key files ready** (llm.py, projects.py, config.py)
- [ ] **Prepare terminal with `show_db.py` ready to run** (optional)

### Have Ready
- [ ] Fresh database (or delete test projects for clean demo)
- [ ] Both servers running (backend + frontend)
- [ ] PowerPoint and Word applications installed
- [ ] VS Code open with project folder
- [ ] Script printed or on second monitor
- [ ] Water nearby 😊
- [ ] **Files bookmarked/open**: llm.py, projects.py, folder structure

### Backup Plans
- [ ] Have a pre-created project in case AI is slow
- [ ] Screenshot key code sections as backup
- [ ] Test export functionality before recording
- [ ] Have a backup recording if first attempt fails

---

## 📁 Key Files to Show in Video

### Must Show (High Priority)
1. **backend/app/services/llm.py** (lines ~25-60)
   - Show the prompt engineering
   - Highlight model choice and temperature
   - Explain why quality is high

2. **backend/app/routers/projects.py** (lines ~195-238)
   - Show refine_content() function
   - Point to Revision creation
   - Explain audit trail

3. **backend/app/config.py** or **.env**
   - Show environment variables
   - Explain deployment flexibility

4. **Project folder structure** (in VS Code sidebar)
   - Show separation of concerns
   - Highlight modular architecture

### Optional (If Time Permits)
5. **frontend/src/pages/ProjectEditor.jsx**
   - Show React components
   - Explain state management

6. **requirements.txt or package.json**
   - Show pinned dependencies
   - Mention production readiness

7. **Terminal with servers running**
   - Show both backend and frontend active
   - Maybe run `show_db.py` quickly

---

## 🌟 Optional Extensions (If You Want 10+ Minutes)

### Database Inspection (30-60 sec)
**[Open terminal, run show_db.py]**

> "Let me show you the database persistence. I'll run this utility script..."

**[Show output]**

> "See? 41 sections, 7 revisions - complete audit trail with prompts and content history. Every refinement tracked."

### Manual vs AI Workflow (30 sec)
**[Show manual section creation]**

> "You're not forced to use AI suggestions - you can manually build your structure too. Full flexibility."

### Template Comparison (30 sec)
**[Show different templates side-by-side]**

> "Same content, different templates - adapts to your brand and context instantly."

---

## 🎬 Final Notes

**Remember**: 
- This is for Ocean AI interview - show both product AND engineering skills
- Balance demo with code walkthrough (60% demo / 40% code is good)
- Technical evaluators want to see **architecture decisions** and **code quality**
- Don't just show features - explain **why you built it this way**
- Highlight what makes your code **production-ready** vs prototype
- End with confidence - you built something impressive!

**Key Message**: "This isn't just an AI wrapper - it's a well-architected, production-ready platform with thoughtful prompt engineering, data integrity, and clean code."

**Good luck with your Ocean AI interview! 🚀**
