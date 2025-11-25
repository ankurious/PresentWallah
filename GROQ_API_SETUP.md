# How to Get Your Groq API Key

## Step 1: Create Groq Account

1. Go to https://console.groq.com
2. Click "Sign Up" or "Get Started"
3. Sign up with:
   - Google account, or
   - GitHub account, or
   - Email address

## Step 2: Access API Keys

1. After logging in, navigate to: https://console.groq.com/keys
2. You should see "API Keys" page

## Step 3: Create New API Key

1. Click "Create API Key" button
2. Give it a name (e.g., "PresentWallah Development")
3. Click "Create"
4. **IMPORTANT**: Copy the API key immediately
   - It will only be shown once!
   - Format: `gsk_...` (starts with gsk_)

## Step 4: Add to Your Project

1. Open `backend/.env` file in a text editor
2. Find the line: `GROQ_API_KEY=your-groq-api-key-here`
3. Replace with your actual key:
   ```
   GROQ_API_KEY=gsk_your_actual_key_here
   ```
4. Save the file

## Step 5: Verify Setup

1. Start your backend server:
   ```powershell
   cd backend
   .\venv\Scripts\Activate.ps1
   uvicorn main:app --reload
   ```

2. Check for errors in the console
3. If you see no errors, the key is configured correctly!

## Example .env File

Your complete `.env` file should look like this:

```env
SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
GROQ_API_KEY=gsk_abcdefghijklmnopqrstuvwxyz1234567890
DATABASE_URL=sqlite:///./presentwallah.db
```

## Troubleshooting

### "Invalid API Key" Error
- Double-check you copied the entire key
- Ensure no extra spaces before/after the key
- Make sure the key starts with `gsk_`

### "API Key Not Found" Error
- Verify the `.env` file is in the `backend` directory
- Restart the backend server after adding the key

### Rate Limit Errors
- Free tier has rate limits
- Wait a minute and try again
- Consider upgrading your Groq plan

## API Key Security

⚠️ **IMPORTANT SECURITY NOTES:**

1. **Never commit .env to Git**
   - It's already in `.gitignore`
   - Never share your API key publicly

2. **Rotate Keys Regularly**
   - Create new keys periodically
   - Delete old unused keys

3. **Use Different Keys for Different Environments**
   - Development key
   - Production key
   - Testing key

4. **Monitor Usage**
   - Check Groq console for usage
   - Set up alerts if available

## Free Tier Limits (as of 2025)

- Model: llama-3.3-70b-versatile (used by PresentWallah)
- Requests per minute: ~30
- Tokens per minute: varies
- Cost: FREE

For production use, consider:
- Monitoring your usage
- Implementing rate limiting
- Upgrading to paid tier if needed

## Alternative: Environment Variable

Instead of `.env` file, you can set as system environment variable:

**Windows PowerShell:**
```powershell
$env:GROQ_API_KEY="gsk_your_key_here"
```

**Windows Command Prompt:**
```cmd
set GROQ_API_KEY=gsk_your_key_here
```

## Need Help?

- Groq Documentation: https://console.groq.com/docs
- Groq Discord: https://discord.gg/groq
- Check our README.md troubleshooting section

## Quick Test

Test your API key with this Python script:

```python
# test_groq.py
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

try:
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": "Hello!"}],
        model="llama-3.1-70b-versatile",
    )
    print("✅ API Key is working!")
    print(f"Response: {response.choices[0].message.content}")
except Exception as e:
    print(f"❌ Error: {e}")
```

Run it:
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python test_groq.py
```
