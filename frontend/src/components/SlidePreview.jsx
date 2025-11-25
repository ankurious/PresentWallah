import React, { useState, useEffect } from 'react';
import './SlidePreview.css';

const TEMPLATE_COLORS = {
  modern: {
    primary: 'rgb(15, 32, 96)',
    secondary: 'rgb(30, 58, 138)',
    accent: 'rgb(220, 230, 255)'
  },
  minimal: {
    primary: 'rgb(70, 70, 70)',
    secondary: 'rgb(100, 100, 100)',
    accent: 'rgb(230, 230, 230)'
  },
  corporate: {
    primary: 'rgb(0, 82, 155)',
    secondary: 'rgb(30, 110, 180)',
    accent: 'rgb(200, 230, 255)'
  },
  creative: {
    primary: 'rgb(102, 16, 150)',
    secondary: 'rgb(130, 50, 180)',
    accent: 'rgb(240, 220, 255)'
  }
};

function SlidePreview({ section, isFirstSlide, mainTopic, template = 'modern' }) {
  const [imageUrl, setImageUrl] = useState(null);
  const [imageLoading, setImageLoading] = useState(true);
  
  const colors = TEMPLATE_COLORS[template] || TEMPLATE_COLORS.modern;

  useEffect(() => {
    fetchImage();
  }, [section.title]);

  const fetchImage = async () => {
    if (isFirstSlide) {
      setImageLoading(false);
      return;
    }

    setImageLoading(true);
    try {
      // Use Pexels API to get image
      const PEXELS_API_KEY = '7NmYpMktvDJMB4UgaVw6JFqF2RBtWzXHGYqHIr7t3PSPG1JNN1Mcy39D';
      const queries = [section.title, `${section.title} business`, `${section.title} professional`];
      
      for (const query of queries) {
        const response = await fetch(
          `https://api.pexels.com/v1/search?query=${encodeURIComponent(query)}&per_page=1&orientation=landscape`,
          {
            headers: {
              Authorization: PEXELS_API_KEY
            }
          }
        );
        
        if (response.ok) {
          const data = await response.json();
          if (data.photos && data.photos.length > 0) {
            setImageUrl(data.photos[0].src.large);
            break;
          }
        }
      }
    } catch (error) {
      console.error('Error fetching image:', error);
    } finally {
      setImageLoading(false);
    }
  };

  const parseBulletPoints = (content) => {
    if (!content) return [];
    return content
      .split('\n')
      .map(line => line.trim())
      .filter(line => line.length > 0)
      .map(line => line.replace(/^[•\-*►▪]\s*/, ''));
  };

  if (isFirstSlide) {
    return (
      <div className="slide-preview title-slide" style={{
        background: `linear-gradient(135deg, ${colors.primary} 0%, ${colors.secondary} 100%)`
      }}>
        <div className="title-slide-content">
          <h1 className="preview-title">{section.title}</h1>
          <p className="preview-subtitle" style={{ color: colors.accent }}>{mainTopic}</p>
        </div>
      </div>
    );
  }

  const bullets = parseBulletPoints(section.content);

  return (
    <div className="slide-preview content-slide">
      <div className="slide-header" style={{ background: colors.primary }}>
        <h2>{section.title}</h2>
      </div>
      
      <div className="slide-body">
        {imageLoading ? (
          <div className="image-placeholder loading">
            <div className="spinner"></div>
            <p>Loading image...</p>
          </div>
        ) : imageUrl ? (
          <div className="slide-image">
            <img src={imageUrl} alt={section.title} />
          </div>
        ) : (
          <div className="image-placeholder">
            <p>📷 No image available</p>
          </div>
        )}
        
        <div className="slide-content">
          {section.content ? (
            <ul className="bullet-list">
              {bullets.map((bullet, index) => (
                <li key={index}>{bullet}</li>
              ))}
            </ul>
          ) : (
            <p className="no-content">Content not generated yet</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default SlidePreview;
