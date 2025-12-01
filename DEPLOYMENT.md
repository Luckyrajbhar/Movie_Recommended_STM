# Deployment Guide

## Quick Deployment Checklist

Before deploying, ensure you have:

- [x] `requirements.txt` - Created ✓
- [x] `.streamlit/config.toml` - Created ✓
- [ ] `similarity.pkl` - **MISSING - REQUIRED FOR APP TO WORK**
- [x] `movies.pkl` - Present ✓
- [x] `app.py` - Present ✓

## Streamlit Cloud Deployment (Recommended)

### Step 1: Prepare Your Repository

1. Make sure all files are ready:
   ```
   app.py
   movies.pkl
   similarity.pkl  ← YOU NEED THIS FILE
   movie_dict.pkl (optional)
   requirements.txt
   .streamlit/config.toml
   ```

2. Create a `.gitignore` file (optional but recommended):
   ```
   __pycache__/
   *.pyc
   .venv/
   env/
   *.log
   ```

### Step 2: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit - Movie Recommendation App"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### Step 3: Deploy on Streamlit Cloud

1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Fill in:
   - Repository: Select your repository
   - Branch: `main`
   - Main file path: `app.py`
5. Click "Deploy"

### Step 4: Access Your App

Your app will be available at:
```
https://YOUR_APP_NAME.streamlit.app
```

## Important Note

⚠️ **The `similarity.pkl` file is missing from your project.** This file is required for the app to function. You need to:

1. Generate this file from your notebook (`movie_recomender_system.ipynb`), OR
2. Ensure it's included in your repository before deploying

Without `similarity.pkl`, the app will crash when trying to load recommendations.

## Alternative Deployment Options

### Railway

1. Install Railway CLI: `npm i -g @railway/cli`
2. Login: `railway login`
3. Initialize: `railway init`
4. Deploy: `railway up`

### Render

1. Create account at render.com
2. Create new Web Service
3. Connect GitHub repository
4. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run app.py --server.port=$PORT`
5. Deploy

## Troubleshooting

- **Module not found errors**: Ensure all dependencies are in `requirements.txt`
- **File not found errors**: Check all `.pkl` files are in repository
- **Memory errors**: Your `.pkl` files may be too large for free tiers

