# Testing Guide for PresentWallah Platform

## Manual Testing Checklist

### 1. Authentication Tests

#### Registration
- [ ] Navigate to http://localhost:3000
- [ ] Click "Sign Up"
- [ ] Test validation:
  - [ ] Empty fields show error
  - [ ] Invalid email format shows error
  - [ ] Password mismatch shows error
  - [ ] Short password (< 6 chars) shows error
- [ ] Register with valid credentials:
  - Email: test@example.com
  - Username: testuser
  - Password: test123456
- [ ] Verify successful registration message
- [ ] Verify redirect to login page

#### Login
- [ ] Enter registered credentials
- [ ] Verify successful login
- [ ] Verify redirect to dashboard
- [ ] Check that username appears in navbar

#### Token Persistence
- [ ] Refresh the page
- [ ] Verify still logged in
- [ ] Open browser dev tools → Application → Local Storage
- [ ] Verify token exists

#### Logout
- [ ] Click logout button
- [ ] Verify redirect to login
- [ ] Verify token removed from localStorage
- [ ] Try accessing /dashboard directly
- [ ] Verify redirect back to login

### 2. Project Management Tests

#### Dashboard
- [ ] View empty dashboard (no projects)
- [ ] See "No projects yet" message
- [ ] Click "+ New Project" button

#### Create Word Document Project
- [ ] Click Word Document card
- [ ] Enter project details:
  - Title: "Q4 Business Report"
  - Topic: "Quarterly performance analysis for tech startup"
- [ ] Test manual section creation:
  - [ ] Click "+ Add Section"
  - [ ] Enter section title: "Executive Summary"
  - [ ] Add 3-4 more sections
  - [ ] Test reordering with ↑/↓ buttons
  - [ ] Test deletion with × button
- [ ] Click "Create Project"
- [ ] Verify redirect to project editor

#### Create PowerPoint Project
- [ ] Return to dashboard
- [ ] Click "+ New Project"
- [ ] Click PowerPoint Presentation card
- [ ] Enter project details:
  - Title: "Marketing Strategy 2025"
  - Topic: "Comprehensive marketing strategy for product launch"
- [ ] Test AI-Suggest feature:
  - [ ] Click "🤖 AI-Suggest Outline"
  - [ ] Wait for AI suggestions
  - [ ] Verify 8 slide titles generated
  - [ ] Edit one slide title manually
  - [ ] Add one more slide manually
- [ ] Click "Create Project"

#### Delete Project
- [ ] Return to dashboard
- [ ] Click × button on a project card
- [ ] Confirm deletion
- [ ] Verify project removed from list

### 3. Content Generation Tests

#### Generate Content
- [ ] Open a project
- [ ] Click "🤖 Generate Content" button
- [ ] Wait for generation (may take 30-60 seconds)
- [ ] Verify content appears for all sections
- [ ] Check that content is relevant to:
  - [ ] Section title
  - [ ] Main topic
  - [ ] Document type (paragraphs for Word, bullets for PPT)

#### Content Quality Checks
For Word documents:
- [ ] Content is 200-400 words per section
- [ ] Proper paragraph formatting
- [ ] Professional language

For PowerPoint:
- [ ] Content is 3-6 bullet points per slide
- [ ] Concise points (10-20 words each)
- [ ] Presentation-ready format

### 4. Refinement Tests

#### Section Navigation
- [ ] Click different sections in sidebar
- [ ] Verify content updates in main area
- [ ] Verify active section highlighted

#### AI Refinement
- [ ] Select a section with content
- [ ] Enter refinement prompts and test:
  - [ ] "Make this more formal"
  - [ ] "Add bullet points"
  - [ ] "Shorten to 100 words"
  - [ ] "Add specific statistics and numbers"
  - [ ] "Convert to conversational tone"
- [ ] For each refinement:
  - [ ] Wait for AI response
  - [ ] Verify content updated
  - [ ] Verify new content matches request

#### Feedback System
- [ ] Click 👍 (Like) button
- [ ] Verify button becomes active/highlighted
- [ ] Refresh page
- [ ] Verify like status persists
- [ ] Click 👎 (Dislike) button
- [ ] Verify button becomes active
- [ ] Check sidebar shows feedback icon

#### Comments
- [ ] Enter comment: "This section needs more data"
- [ ] Wait a moment (auto-saves)
- [ ] Refresh page
- [ ] Verify comment persists
- [ ] Update comment
- [ ] Verify update saves

### 5. Export Tests

#### Export Word Document
- [ ] Open a Word project with generated content
- [ ] Click "📥 Export Document"
- [ ] Wait for download
- [ ] Verify .docx file downloads
- [ ] Open file in Microsoft Word
- [ ] Verify:
  - [ ] Title appears as heading
  - [ ] All sections present
  - [ ] Content matches what's in editor
  - [ ] Proper formatting

#### Export PowerPoint
- [ ] Open a PowerPoint project
- [ ] Click "📥 Export Document"
- [ ] Verify .pptx file downloads
- [ ] Open file in Microsoft PowerPoint
- [ ] Verify:
  - [ ] First slide is title slide
  - [ ] All slides present
  - [ ] Content matches editor
  - [ ] Bullet points formatted correctly

### 6. Error Handling Tests

#### API Errors
- [ ] Stop backend server
- [ ] Try to create project
- [ ] Verify error message shown
- [ ] Restart backend
- [ ] Verify functionality restored

#### Invalid API Key
- [ ] Set invalid GROQ_API_KEY in .env
- [ ] Try to generate content
- [ ] Verify error message (in browser console or backend logs)
- [ ] Restore valid API key

#### Empty Content Refinement
- [ ] Try to refine without entering prompt
- [ ] Verify alert shown

#### Network Issues
- [ ] Open browser Network tab
- [ ] Throttle to "Slow 3G"
- [ ] Test content generation
- [ ] Verify loading states work properly

### 7. Edge Cases

#### Long Content
- [ ] Create project with many sections (10+)
- [ ] Generate all content
- [ ] Verify performance is acceptable
- [ ] Verify all sections load

#### Special Characters
- [ ] Create project with title: "Q4 Report: Tech & AI (2025)"
- [ ] Add section: "Cost/Benefit Analysis"
- [ ] Generate and export
- [ ] Verify special characters handled correctly

#### Empty Projects
- [ ] Create project with 1 section
- [ ] Export without generating content
- [ ] Verify document exports with placeholder text

#### Concurrent Refinements
- [ ] Start refining a section
- [ ] Immediately switch to another section
- [ ] Verify no errors occur

### 8. UI/UX Tests

#### Responsive Design
- [ ] Resize browser to mobile width (375px)
- [ ] Verify layout adapts
- [ ] Test all main pages
- [ ] Test on actual mobile device

#### Loading States
- [ ] Verify loading indicators show during:
  - [ ] Login
  - [ ] Registration
  - [ ] Content generation
  - [ ] Refinement
  - [ ] Export

#### Visual Feedback
- [ ] Hover over buttons
- [ ] Verify hover effects work
- [ ] Click buttons
- [ ] Verify click feedback

### 9. Performance Tests

#### Multiple Projects
- [ ] Create 5-10 projects
- [ ] Verify dashboard loads quickly
- [ ] Verify no lag when clicking projects

#### Large Sections
- [ ] Generate content for project with 8+ sections
- [ ] Verify generation completes
- [ ] Verify editor remains responsive

### 10. Security Tests

#### Protected Routes
- [ ] Logout
- [ ] Try to access /dashboard directly
- [ ] Verify redirect to login
- [ ] Try /project/1
- [ ] Verify redirect to login

#### Token Expiration
- [ ] Login
- [ ] Wait 30+ minutes (token expiry time)
- [ ] Try to make API call
- [ ] Verify token expired (401 error)
- [ ] Login again

#### SQL Injection Attempt
- [ ] Try username: `admin' OR '1'='1`
- [ ] Verify rejected/sanitized

## Automated Testing (Future)

### Backend Tests (pytest)
```python
# tests/test_auth.py
def test_user_registration():
    pass

def test_user_login():
    pass

def test_protected_endpoint():
    pass

# tests/test_projects.py
def test_create_project():
    pass

def test_generate_content():
    pass

def test_refine_content():
    pass
```

### Frontend Tests (Jest/React Testing Library)
```javascript
// tests/Login.test.jsx
describe('Login Component', () => {
  test('renders login form', () => {});
  test('submits credentials', () => {});
});
```

## Performance Benchmarks

Expected response times:
- Login: < 500ms
- Create project: < 300ms
- Generate content (per section): 2-5 seconds
- Refine content: 2-5 seconds
- Export document: < 1 second

## Browser Compatibility

Test on:
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Edge (latest)
- [ ] Safari (if available)

## Known Limitations

1. Groq API rate limits may affect bulk operations
2. Large documents (20+ sections) may take longer to generate
3. Token expires after 30 minutes (configurable)

## Bug Reporting Template

```
**Description:**
[What happened?]

**Steps to Reproduce:**
1. 
2. 
3. 

**Expected Behavior:**
[What should have happened?]

**Actual Behavior:**
[What actually happened?]

**Environment:**
- Browser: 
- OS: 
- Frontend Version: 
- Backend Version: 

**Screenshots/Logs:**
[Attach if applicable]
```

## Test Results Template

```
Date: ________________
Tester: ______________

Authentication: ☐ PASS ☐ FAIL
Project Management: ☐ PASS ☐ FAIL
Content Generation: ☐ PASS ☐ FAIL
Refinement: ☐ PASS ☐ FAIL
Export: ☐ PASS ☐ FAIL

Issues Found: _______________
Overall Status: ☐ PASS ☐ FAIL

Notes:
```
