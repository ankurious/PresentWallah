# Template System Guide

## Overview
PresentWallah now includes a **multi-template system** for PowerPoint presentations, allowing you to choose from 4 professionally designed color schemes and customize font sizes.

## Important Clarifications

### What AI Can Control
✅ **Content Generation**: AI generates slide titles and bullet point content  
✅ **Content Refinement**: AI can rewrite, expand, simplify, or improve text  
✅ **Structure**: AI suggests slide outlines and section organization

### What AI Cannot Control
❌ **Images**: Images are automatically fetched from Pexels based on slide titles (not AI-controlled)  
❌ **Templates**: Color schemes are project settings (not AI-controlled)  
❌ **Font Sizes**: Text size is a project setting (not AI-controlled)

**Why?** The separation ensures that:
- AI focuses on content quality (what it does best)
- Visual styling remains consistent across all slides
- Users have direct control over presentation appearance

## Available Templates

### 1. Modern (Navy Blue) - DEFAULT
- **Primary Color**: Deep navy blue (`#0F2060`)
- **Secondary Color**: Medium blue (`#1E3A8A`)
- **Accent Color**: Light blue (`#DCE6FF`)
- **Best For**: Professional business presentations, corporate reports

### 2. Minimal (Gray)
- **Primary Color**: Dark gray (`#464646`)
- **Secondary Color**: Medium gray (`#646464`)
- **Accent Color**: Light gray (`#E6E6E6`)
- **Best For**: Clean, minimalist presentations, academic papers

### 3. Corporate (Blue)
- **Primary Color**: Corporate blue (`#00529B`)
- **Secondary Color**: Sky blue (`#1E6EB4`)
- **Accent Color**: Pale blue (`#C8E6FF`)
- **Best For**: Traditional business settings, client presentations

### 4. Creative (Purple)
- **Primary Color**: Deep purple (`#661096`)
- **Secondary Color**: Medium purple (`#8232B4`)
- **Accent Color**: Lavender (`#F0DCFF`)
- **Best For**: Creative agencies, marketing decks, innovative projects

## How to Use

### When Creating a New Project
1. Select **PowerPoint Presentation** as document type
2. Fill in project title and main topic
3. **Choose Template**: Select from the dropdown (Modern/Minimal/Corporate/Creative)
4. **Adjust Font Size**: Use the slider (16pt - 28pt, default: 20pt)
5. Add slides and create project

### Changing Settings After Creation
Currently, template and font size are set during project creation. Future updates may include:
- In-editor template switcher
- Per-slide font customization
- Custom color scheme builder

## Font Size Guidelines

| Size | Use Case |
|------|----------|
| 16pt | Dense content, maximum text per slide |
| 18pt | Detailed information, reports |
| **20pt** | **Default - balanced readability** |
| 24pt | Important points, executive summaries |
| 28pt | Large audience, minimal text |

## AI Refinement Tips

Since AI controls **content only**, use these prompts for best results:

### Good AI Refinement Prompts
✅ "Make this more formal"  
✅ "Add 2 more bullet points"  
✅ "Simplify to 3 key points"  
✅ "Make it more persuasive"  
✅ "Add statistics if relevant"

### What to Use Notes/Comments For
Instead of asking AI to change styling, use the **Notes/Comments** section to:
- Remind yourself to add specific images
- Note font size changes for future versions
- Mark slides that need different templates
- Document sources and references

## Live Preview

The **Live Preview** feature shows:
- Template colors applied to slide backgrounds and headers
- Pexels images (fetched in real-time)
- Bullet points formatted as they'll appear in export
- Accurate representation of final presentation

**Note**: Preview matches export appearance exactly, including template colors and image placement.

## Technical Details

### Template Color Application
- **Title Slides**: Full gradient background using primary → secondary colors
- **Content Slides**: Header bar in primary color, white background for text
- **Accent Colors**: Used for subtitles and decorative elements

### Image Selection
Images are automatically selected based on:
1. Slide title (exact match)
2. Slide title + "business"
3. Slide title + "professional"

The system tries multiple queries to find the best match, with 200 requests/hour limit from Pexels.

### Font Application
Font size applies to:
- Bullet point text on content slides
- Body text in Word documents (when applicable)

Title text sizes are fixed for visual hierarchy:
- Main titles: 60pt (title slides) / 36pt (content slides)
- Subtitles: 28pt

## Frequently Asked Questions

**Q: Can I change the template after creating a project?**  
A: Not yet. Choose carefully during creation, or create a new project with different settings.

**Q: Why can't AI change fonts and images?**  
A: AI excels at content quality, not visual design. Separating concerns gives you better control and consistency.

**Q: What if I don't like the auto-selected images?**  
A: Images are based on slide titles. Refine slide titles to get better image matches (e.g., "Market Growth" → "Financial Market Growth Charts").

**Q: Can I add custom templates?**  
A: Not currently. The 4 templates cover most professional use cases. Custom templates may be added in future updates.

**Q: Do templates apply to Word documents?**  
A: No, templates are PowerPoint-only. Word documents use standard formatting with proper heading styles.

## Best Practices

1. **Choose Template First**: Pick a template that matches your audience and purpose before generating content
2. **Consistent Titles**: Use clear, descriptive slide titles for better image matching
3. **Font Size for Audience**: Larger rooms need larger text (24-28pt), smaller meetings can use 18-20pt
4. **AI for Content**: Use AI refinement for content improvement, not styling requests
5. **Preview Before Export**: Always check live preview to ensure images and colors meet expectations

## Future Enhancements

Planned features (not yet implemented):
- Per-slide template override
- Custom color schemes
- Font family selection
- Template preview gallery
- Bulk template changes for existing projects

---

**Last Updated**: January 2025  
**Version**: 1.0
