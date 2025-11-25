# Pexels API Setup Guide

## Why Pexels?
Pexels provides **free, high-quality stock photos** perfect for PowerPoint presentations. The API is completely free with generous limits.

## Get Your Free API Key

### Step 1: Create Account
1. Go to https://www.pexels.com/
2. Click "Join" in the top right
3. Sign up with email or Google account (takes 30 seconds)

### Step 2: Get API Key
1. Visit https://www.pexels.com/api/
2. Click "Get Started" or "Your API Key"
3. Copy your API key (looks like: `abcd1234efgh5678ijkl9012mnop3456`)

### Step 3: Add to Your Project
1. Open `backend/.env` file
2. Replace `your-pexels-api-key-here` with your actual API key:
   ```
   PEXELS_API_KEY=abcd1234efgh5678ijkl9012mnop3456
   ```
3. Save the file
4. Restart the backend server

## API Limits (Free Tier)
- ✅ **200 requests per hour**
- ✅ **Unlimited requests per month**
- ✅ **No credit card required**
- ✅ **Commercial use allowed**

## Features Enabled
When you add the Pexels API key, your presentations will automatically:
- 📸 Include relevant stock photos for each slide
- 🎨 Use professional slide layouts with image + content
- ✨ Create presentation-ready slides like Gamma AI

## Testing
After adding the API key:
1. Create a new PowerPoint project
2. Generate content for slides
3. Export the presentation
4. Each slide will have a relevant image from Pexels!

## Troubleshooting
- **No images appearing?** Check that your API key is correct in `.env`
- **API limit reached?** Free tier gives 200/hour - more than enough for testing
- **Want to disable images?** The app works fine without the API key (just no images)

## Alternative (Optional)
If you don't want to use Pexels, the app will still work perfectly - presentations will just have text without images.
