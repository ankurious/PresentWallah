import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { projectAPI } from '../services/api';
import SlidePreview from '../components/SlidePreview';
import './ProjectEditor.css';

function ProjectEditor() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [project, setProject] = useState(null);
  const [loading, setLoading] = useState(true);
  const [generating, setGenerating] = useState(false);
  const [exporting, setExporting] = useState(false);
  const [selectedSection, setSelectedSection] = useState(null);
  const [refinementPrompt, setRefinementPrompt] = useState('');
  const [refining, setRefining] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    loadProject();
  }, [id]);

  const loadProject = async () => {
    try {
      const response = await projectAPI.get(id);
      setProject(response.data);
      if (response.data.sections.length > 0) {
        setSelectedSection(response.data.sections[0].id);
      }
    } catch (err) {
      setError('Failed to load project');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleGenerateContent = async () => {
    setGenerating(true);
    try {
      const response = await projectAPI.generateContent(parseInt(id));
      setProject(response.data);
    } catch (err) {
      alert('Failed to generate content');
      console.error(err);
    } finally {
      setGenerating(false);
    }
  };

  const handleRefineContent = async () => {
    if (!refinementPrompt.trim()) {
      alert('Please enter a refinement prompt');
      return;
    }

    setRefining(true);
    try {
      const response = await projectAPI.refineContent(selectedSection, refinementPrompt);
      // Update the section in project
      setProject(prev => ({
        ...prev,
        sections: prev.sections.map(s => 
          s.id === selectedSection ? response.data : s
        )
      }));
      setRefinementPrompt('');
    } catch (err) {
      alert('Failed to refine content');
      console.error(err);
    } finally {
      setRefining(false);
    }
  };

  const handleLikeDislike = async (sectionId, liked) => {
    try {
      await projectAPI.updateSection(sectionId, { liked });
      setProject(prev => ({
        ...prev,
        sections: prev.sections.map(s => 
          s.id === sectionId ? { ...s, liked } : s
        )
      }));
    } catch (err) {
      alert('Failed to update feedback');
      console.error(err);
    }
  };

  const handleCommentUpdate = async (sectionId, comment) => {
    try {
      await projectAPI.updateSection(sectionId, { comment });
      setProject(prev => ({
        ...prev,
        sections: prev.sections.map(s => 
          s.id === sectionId ? { ...s, comment } : s
        )
      }));
    } catch (err) {
      console.error('Failed to update comment:', err);
    }
  };

  const handleExport = async () => {
    setExporting(true);
    try {
      const response = await projectAPI.export(id);
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      const extension = project.document_type === 'docx' ? '.docx' : '.pptx';
      link.setAttribute('download', `${project.title}${extension}`);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (err) {
      alert('Failed to export document');
      console.error(err);
    } finally {
      setExporting(false);
    }
  };

  const getCurrentSection = () => {
    return project?.sections.find(s => s.id === selectedSection);
  };

  const hasContent = project?.sections.some(s => s.content);

  if (loading) {
    return (
      <div className="editor-container">
        <div className="loading">Loading project...</div>
      </div>
    );
  }

  if (error || !project) {
    return (
      <div className="editor-container">
        <div className="error">{error || 'Project not found'}</div>
      </div>
    );
  }

  const currentSection = getCurrentSection();

  return (
    <div className="editor-container">
      <nav className="editor-nav">
        <div className="nav-left">
          <button onClick={() => navigate('/dashboard')} className="back-button">
            ← Dashboard
          </button>
          <div className="project-info">
            <h1>{project.title}</h1>
            <span className="doc-type-badge">{project.document_type.toUpperCase()}</span>
          </div>
        </div>
        <div className="nav-actions">
          {!hasContent && (
            <button 
              onClick={handleGenerateContent} 
              className="generate-button"
              disabled={generating}
            >
              {generating ? 'Generating...' : 'Generate Content'}
            </button>
          )}
          {hasContent && (
            <button 
              onClick={handleExport} 
              className="export-button"
              disabled={exporting}
            >
              {exporting ? 'Exporting...' : 'Export Document'}
            </button>
          )}
        </div>
      </nav>

      <div className="editor-content">
        <div className="sidebar">
          <h3>{project.document_type === 'docx' ? 'Sections' : 'Slides'}</h3>
          <div className="sections-list">
            {project.sections.map((section, index) => (
              <div
                key={section.id}
                className={`section-item ${selectedSection === section.id ? 'active' : ''}`}
                onClick={() => setSelectedSection(section.id)}
              >
                <div className="section-number">{index + 1}</div>
                <div className="section-info">
                  <div className="section-title">{section.title}</div>
                  {section.liked !== null && (
                    <div className="section-feedback">
                      {section.liked ? '👍' : '👎'}
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="main-editor">
          {currentSection && (
            <>
              {/* Live Preview for PowerPoint */}
              {project.document_type === 'pptx' && (
                <div className="preview-section">
                  <h3>Live Preview</h3>
                  <SlidePreview 
                    section={currentSection}
                    isFirstSlide={project.sections.indexOf(currentSection) === 0}
                    mainTopic={project.main_topic}
                    template={project.template || 'modern'}
                  />
                </div>
              )}

              <div className="section-header">
                <h2>{currentSection.title}</h2>
                <div className="feedback-buttons">
                  <button
                    className={`feedback-button ${currentSection.liked === true ? 'active' : ''}`}
                    onClick={() => handleLikeDislike(currentSection.id, true)}
                  >
                    Like
                  </button>
                  <button
                    className={`feedback-button ${currentSection.liked === false ? 'active' : ''}`}
                    onClick={() => handleLikeDislike(currentSection.id, false)}
                  >
                    Dislike
                  </button>
                </div>
              </div>

              <div className="content-area">
                {currentSection.content ? (
                  <div className="content-display">
                    {currentSection.content.split('\n').map((line, i) => (
                      <p key={i}>{line}</p>
                    ))}
                  </div>
                ) : (
                  <div className="no-content">
                    Content not generated yet. Click "Generate Content" to create AI-powered content.
                  </div>
                )}
              </div>

              {currentSection.content && (
                <div className="refinement-section">
                  <h3>AI Refinement</h3>
                  <div className="refinement-input">
                    <textarea
                      value={refinementPrompt}
                      onChange={(e) => setRefinementPrompt(e.target.value)}
                      placeholder="e.g., Make this more formal, Add bullet points, Shorten to 100 words..."
                      rows="3"
                    />
                    <button 
                      onClick={handleRefineContent}
                      disabled={refining}
                      className="refine-button"
                    >
                      {refining ? 'Refining...' : 'Refine Content'}
                    </button>
                  </div>
                </div>
              )}

              <div className="comment-section">
                <h3>Notes / Comments</h3>
                <textarea
                  value={currentSection.comment || ''}
                  onChange={(e) => handleCommentUpdate(currentSection.id, e.target.value)}
                  placeholder="Add your notes or comments about this section..."
                  rows="3"
                  className="comment-textarea"
                />
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
}

export default ProjectEditor;
