# Deployment to Vercel

## Prerequisites
1. GitHub account
2. Vercel account (free tier)

## Steps
1. Push this repository to GitHub:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/leprechaun-generator.git
   git push -u origin main
   ```

2. Deploy on Vercel:
   - Go to https://vercel.com
   - Click "New Project"
   - Import from GitHub
   - Select this repository
   - Configure:
     - Framework Preset: Other
     - Build Command: (leave empty)
     - Output Directory: (leave empty)
     - Install Command: pip install -r requirements.txt
   - Click "Deploy"

3. Environment Variables (optional):
   - Add `SECRET_KEY` for Flask sessions

## Post-deployment
- Test the public URL
- Set up custom domain (optional)
- Monitor logs in Vercel dashboard
