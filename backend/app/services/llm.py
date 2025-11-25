from groq import Groq
from app.config import get_settings
from typing import List

settings = get_settings()

class LLMService:
    def __init__(self):
        self.client = Groq(api_key=settings.groq_api_key)
        # llama-3.3-70b-versatile is the latest and most capable model on Groq
        # Alternative: mixtral-8x7b-32768 for longer context
        self.model = "llama-3.3-70b-versatile"
    
    def generate_content(self, section_title: str, main_topic: str, document_type: str) -> str:
        """Generate content for a specific section/slide"""
        if document_type == "docx":
            prompt = f"""You are a senior business consultant and expert writer with 15+ years of experience creating high-impact business documents for Fortune 500 companies.

CONTEXT:
Main Topic: {main_topic}
Section Focus: "{section_title}"

YOUR TASK:
Write authoritative, data-informed content for this section that demonstrates deep subject matter expertise.

CONTENT REQUIREMENTS:
1. LENGTH: 300-500 words (substantive, not filler)
2. STRUCTURE:
   - Opening statement that hooks with insight or data point
   - 2-3 well-developed paragraphs with concrete examples
   - Practical implications or actionable takeaways
3. QUALITY STANDARDS:
   - Include specific metrics, frameworks, or methodologies where relevant
   - Reference industry best practices or proven approaches
   - Use precise business terminology (avoid vague generalities)
   - Provide actionable insights, not just descriptions
   - Support claims with logical reasoning or implied expertise
4. TONE: Professional, authoritative, strategic (Forbes/HBR caliber)

AVOID:
- Generic statements like "This is important because..."
- Obvious advice or platitudes
- Repetitive phrasing
- Filler words and fluff

Deliver ONLY the section content - no meta-commentary, no section title repetition."""
        else:  # pptx
            prompt = f"""You are a senior strategy consultant creating a C-suite presentation for a Fortune 500 company.

CONTEXT:
Presentation Topic: {main_topic}
Current Slide: "{section_title}"

YOUR TASK:
Create punchy, executive-level bullet points that deliver maximum insight with minimum words.

STRICT FORMATTING RULES:
- Output EXACTLY 4-6 bullet points
- Each bullet MUST start with "• " (bullet symbol + space)
- Length: 8-15 words per bullet (concise and impactful)
- NO paragraphs, NO numbered lists, NO extra text

CONTENT QUALITY STANDARDS:
- Lead with strong action verbs or specific metrics
- Use precise business language (KPIs, ROI, scalability, etc.)
- Include concrete elements: numbers, percentages, frameworks, or outcomes
- Focus on strategic insights, not generic observations
- Make each bullet deliver distinct value (no redundancy)

EXAMPLES OF EXCELLENT BULLETS:
• Implement AI-driven analytics to reduce operational costs by 30%
• Leverage agile methodology for faster time-to-market execution
• Establish cross-functional teams to drive innovation initiatives
• Deploy predictive modeling to optimize resource allocation
• Scale infrastructure using cloud-native architecture patterns

AVOID:
- Vague statements ("Improve efficiency", "Enhance performance")
- Obvious points ("This is important", "We should focus on")
- Repetitive phrasing across bullets
- Starting every bullet the same way

Deliver ONLY the bullet points in the exact format shown - nothing else."""
        
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=self.model,
                temperature=0.6,  # Lower for more focused, professional output
                max_tokens=1024
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error generating content: {str(e)}"
    
    def refine_content(self, current_content: str, refinement_prompt: str, section_title: str, document_type: str = "pptx") -> str:
        """Refine existing content based on user prompt"""
        if document_type == "pptx":
            prompt = f"""You are a senior presentation coach refining executive-level slides.

CURRENT SLIDE: "{section_title}"

EXISTING BULLETS:
{current_content}

USER'S REFINEMENT REQUEST:
{refinement_prompt}

YOUR TASK:
Revise the bullet points to address the user's request while maintaining C-suite quality.

STRICT FORMATTING RULES:
- Return EXACTLY 4-6 bullet points
- Each bullet MUST start with "• " (bullet symbol + space)
- Length: 8-15 words per bullet
- NO paragraphs, NO numbered lists, NO meta-commentary

QUALITY STANDARDS:
- Keep the strategic, executive tone
- Use precise business terminology and metrics where relevant
- Ensure bullets are distinct and non-redundant
- Lead with action verbs or concrete elements
- Incorporate the user's feedback while maintaining professionalism

Deliver ONLY the revised bullet points - nothing else."""
        else:
            prompt = f"""You are a senior business consultant refining document content for executive review.

SECTION: "{section_title}"

CURRENT CONTENT:
{current_content}

USER'S REFINEMENT REQUEST:
{refinement_prompt}

YOUR TASK:
Revise the content to address the user's feedback while maintaining high professional standards.

REQUIREMENTS:
- Incorporate the user's specific requests/changes
- Maintain authoritative, strategic tone
- Keep concrete examples, metrics, and frameworks
- Ensure logical flow and coherence
- Preserve word count (300-500 words) and paragraph structure
- Use precise business language

Deliver ONLY the refined content - no explanations or meta-commentary."""
        
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=self.model,
                temperature=0.6,  # Lower for more controlled refinement
                max_tokens=1024
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error refining content: {str(e)}"
    
    def suggest_outline(self, main_topic: str, document_type: str, num_items: int = None) -> List[str]:
        """Generate suggested section titles or slide titles"""
        if document_type == "docx":
            prompt = f"""You are a senior business consultant structuring a high-impact document.

TOPIC: {main_topic}

YOUR TASK:
Create a logical, comprehensive document outline with 6-8 section titles that would impress executive stakeholders.

REQUIREMENTS:
- Start with an executive summary or introduction section
- Build a logical narrative flow (context → analysis → strategy → action)
- Use clear, professional section titles (not vague)
- Each title should indicate specific value/content
- End with conclusions, recommendations, or next steps
- Avoid generic titles like "Overview" or "Background"

EXAMPLE QUALITY:
Instead of: "Introduction"
Use: "Market Landscape and Strategic Imperatives"

Instead of: "Analysis"
Use: "Competitive Positioning and Gap Analysis"

Provide ONLY the section titles, one per line, no numbering, no bullets, no extra text."""
        else:  # pptx
            num_slides = num_items or 8
            prompt = f"""You are a senior strategy consultant creating a presentation outline for C-suite executives.

TOPIC: {main_topic}

YOUR TASK:
Create exactly {num_slides} impactful slide titles that tell a clear, compelling story.

SLIDE STRUCTURE:
1. Title slide with hook (not just topic name)
2-3. Context/problem definition slides
4-6. Core analysis/strategy slides
7. Conclusions or recommendations
8. Next steps or call-to-action

TITLE QUALITY STANDARDS:
- Each title: 3-7 words, punchy and specific
- Use action-oriented or insight-driven language
- Avoid generic labels ("Introduction", "Overview", "Background")
- Create narrative flow (each slide builds on previous)
- Make titles executive-friendly (strategic, not tactical)

EXAMPLES OF STRONG TITLES:
- "Market Disruption: AI's $2T Opportunity"
- "Three Critical Capability Gaps"
- "Strategic Roadmap: 18-Month Timeline"
- "ROI Projections and Success Metrics"

Provide ONLY the slide titles, one per line, no numbering, no bullets, no extra commentary."""
        
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=self.model,
                temperature=0.7,  # Slightly higher for creative title generation
                max_tokens=512
            )
            content = response.choices[0].message.content.strip()
            # Split by lines and clean up
            titles = [line.strip() for line in content.split('\n') if line.strip()]
            return titles
        except Exception as e:
            return [f"Error generating outline: {str(e)}"]

llm_service = LLMService()
