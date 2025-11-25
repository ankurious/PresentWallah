import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { projectAPI } from '../services/api';
import './CreateProject.css';

function CreateProject() {
  const [step, setStep] = useState(1);
  const [documentType, setDocumentType] = useState('');
  const [title, setTitle] = useState('');
  const [mainTopic, setMainTopic] = useState('');
  const [sections, setSections] = useState([]);
  const [template, setTemplate] = useState('modern');
  const [fontSize, setFontSize] = useState(20);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [aiSuggesting, setAiSuggesting] = useState(false);
  const navigate = useNavigate();

  const handleDocumentTypeSelect = (type) => {
    setDocumentType(type);
    setStep(2);
  };

  const handleAISuggest = async () => {
    if (!mainTopic.trim()) {
      alert('Please enter a main topic first');
      return;
    }

    setAiSuggesting(true);
    try {
      const response = await projectAPI.aiSuggest({
        main_topic: mainTopic,
        document_type: documentType,
        num_items: documentType === 'pptx' ? 8 : undefined
      });
      
      const suggestedSections = response.data.map((title, index) => ({
        title,
        order: index
      }));
      setSections(suggestedSections);
    } catch (err) {
      alert('Failed to get AI suggestions');
      console.error(err);
    } finally {
      setAiSuggesting(false);
    }
  };

  const addSection = () => {
    setSections([...sections, { title: '', order: sections.length }]);
  };

  const updateSectionTitle = (index, title) => {
    const newSections = [...sections];
    newSections[index].title = title;
    setSections(newSections);
  };

  const removeSection = (index) => {
    const newSections = sections.filter((_, i) => i !== index);
    // Update order
    newSections.forEach((section, i) => {
      section.order = i;
    });
    setSections(newSections);
  };

  const moveSectionUp = (index) => {
    if (index === 0) return;
    const newSections = [...sections];
    [newSections[index - 1], newSections[index]] = [newSections[index], newSections[index - 1]];
    newSections.forEach((section, i) => {
      section.order = i;
    });
    setSections(newSections);
  };

  const moveSectionDown = (index) => {
    if (index === sections.length - 1) return;
    const newSections = [...sections];
    [newSections[index], newSections[index + 1]] = [newSections[index + 1], newSections[index]];
    newSections.forEach((section, i) => {
      section.order = i;
    });
    setSections(newSections);
  };

  const handleCreateProject = async () => {
    if (!title.trim()) {
      setError('Please enter a project title');
      return;
    }

    if (sections.length === 0) {
      setError(`Please add at least one ${documentType === 'docx' ? 'section' : 'slide'}`);
      return;
    }

    if (sections.some(s => !s.title.trim())) {
      setError('All sections must have a title');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await projectAPI.create({
        title,
        document_type: documentType,
        main_topic: mainTopic,
        template: documentType === 'pptx' ? template : undefined,
        font_size: documentType === 'pptx' ? fontSize : undefined,
        sections
      });

      navigate(`/project/${response.data.id}`);
    } catch (err) {
      setError('Failed to create project');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="create-project-container">
      <nav className="create-nav">
        <button onClick={() => navigate('/dashboard')} className="back-button">
          ← Back to Dashboard
        </button>
      </nav>

      <div className="create-content">
        <h1 className="create-title">Create New Project</h1>

        {step === 1 && (
          <div className="step-container">
            <h2>Step 1: Choose Document Type</h2>
            <div className="document-types">
              <div 
                className="document-type-card"
                onClick={() => handleDocumentTypeSelect('docx')}
              >
                <div className="document-icon docx">DOC</div>
                <h3>Word Document</h3>
                <p>Create structured business documents with sections</p>
              </div>
              <div 
                className="document-type-card"
                onClick={() => handleDocumentTypeSelect('pptx')}
              >
                <div className="document-icon pptx">PPT</div>
                <h3>PowerPoint Presentation</h3>
                <p>Create engaging presentations with slides</p>
              </div>
            </div>
          </div>
        )}

        {step === 2 && (
          <div className="step-container">
            <h2>Step 2: Configure Your {documentType === 'docx' ? 'Document' : 'Presentation'}</h2>
            
            {error && <div className="error-message">{error}</div>}

            <div className="form-group">
              <label>Project Title</label>
              <input
                type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="e.g., Q4 Business Report"
              />
            </div>

            <div className="form-group">
              <label>Main Topic / Description</label>
              <textarea
                value={mainTopic}
                onChange={(e) => setMainTopic(e.target.value)}
                placeholder="e.g., A comprehensive market analysis of the EV industry in 2025"
                rows="3"
              />
            </div>

            {documentType === 'pptx' && (
              <>
                <div className="form-group">
                  <label>Template Style</label>
                  <select 
                    value={template} 
                    onChange={(e) => setTemplate(e.target.value)}
                    className="template-select"
                  >
                    <option value="modern">Modern (Navy Blue)</option>
                    <option value="minimal">Minimal (Gray)</option>
                    <option value="corporate">Corporate (Blue)</option>
                    <option value="creative">Creative (Purple)</option>
                  </select>
                  <p className="hint-text">Choose a color scheme for your presentation</p>
                </div>

                <div className="form-group">
                  <label>Font Size: {fontSize}pt</label>
                  <input
                    type="range"
                    min="16"
                    max="28"
                    value={fontSize}
                    onChange={(e) => setFontSize(parseInt(e.target.value))}
                    className="font-size-slider"
                  />
                  <p className="hint-text">Adjust text size for better readability</p>
                </div>
              </>
            )}

            <div className="ai-suggest-section">
              <button 
                onClick={handleAISuggest} 
                className="ai-suggest-button"
                disabled={aiSuggesting}
              >
                {aiSuggesting ? 'AI Generating...' : 'AI Suggest Outline'}
              </button>
              <p className="hint-text">Or manually add {documentType === 'docx' ? 'sections' : 'slides'} below</p>
            </div>

            <div className="sections-container">
              <div className="sections-header">
                <h3>{documentType === 'docx' ? 'Sections' : 'Slides'}</h3>
                <button onClick={addSection} className="add-section-button">
                  + Add {documentType === 'docx' ? 'Section' : 'Slide'}
                </button>
              </div>

              {sections.length === 0 ? (
                <div className="empty-sections">
                  No {documentType === 'docx' ? 'sections' : 'slides'} added yet
                </div>
              ) : (
                <div className="sections-list">
                  {sections.map((section, index) => (
                    <div key={index} className="section-item">
                      <div className="section-order">{index + 1}</div>
                      <input
                        type="text"
                        value={section.title}
                        onChange={(e) => updateSectionTitle(index, e.target.value)}
                        placeholder={`${documentType === 'docx' ? 'Section' : 'Slide'} title...`}
                        className="section-input"
                      />
                      <div className="section-actions">
                        <button 
                          onClick={() => moveSectionUp(index)}
                          disabled={index === 0}
                          className="move-button"
                        >
                          ↑
                        </button>
                        <button 
                          onClick={() => moveSectionDown(index)}
                          disabled={index === sections.length - 1}
                          className="move-button"
                        >
                          ↓
                        </button>
                        <button 
                          onClick={() => removeSection(index)}
                          className="remove-button"
                        >
                          ×
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>

            <div className="form-actions">
              <button onClick={() => setStep(1)} className="back-step-button">
                ← Back
              </button>
              <button 
                onClick={handleCreateProject} 
                className="create-project-button"
                disabled={loading}
              >
                {loading ? 'Creating...' : 'Create Project'}
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default CreateProject;
