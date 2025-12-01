# 🚀 Complete Guide: Deploy on Streamlit Cloud

## Step-by-Step Instructions

### Step 1: Go to Streamlit Cloud
Open your web browser and go to:
👉 **https://share.streamlit.io**

---

### Step 2: Sign In
1. Click the **"Sign in"** button (top right corner)
2. Choose **"Continue with GitHub"**
3. Authorize Streamlit to access your GitHub account
4. You'll be redirected to the Streamlit Cloud dashboard

---

### Step 3: Create New App
1. Click the **"New app"** button (usually in the top right or center)
2. You'll see a form to configure your deployment

---

### Step 4: Fill in the Deployment Form

Fill in these details:

#### **Workspace** (if you have multiple workspaces)
- Select your workspace (usually defaults to your personal workspace)

#### **Repository**
- Click the dropdown
- Select: **`Luckyrajbhar/Movie_Recommended_STM`**
- This is your GitHub repository

#### **Branch**
- Select: **`master`**
- (This is the branch name in your GitHub repo)

#### **Main file path**
- Enter: **`app.py`**
- This is your main Streamlit application file

#### **App URL** (Optional)
- Streamlit will auto-generate a URL like: `movie-recommended-stm`
- Or you can customize it to something like: `movie-recommender`
- Final URL will be: `https://movie-recommender.streamlit.app`

---

### Step 5: Deploy
1. Review all your settings
2. Click the **"Deploy"** button at the bottom
3. Wait for deployment (usually 1-3 minutes)

---

### Step 6: Wait for Deployment
You'll see a progress indicator showing:
- 🔄 "Setting up app..."
- 🔄 "Installing dependencies..."
- 🔄 "Starting app..."
- ✅ "Your app is live!"

---

### Step 7: Access Your App
Once deployed, you'll see:
- ✅ Green checkmark indicating success
- A link to your live app: `https://your-app-name.streamlit.app`
- Click the link to open your app!

---

## ⚠️ Troubleshooting

### If deployment fails, check:

#### 1. **Missing similarity.pkl file**
   - **Error**: `FileNotFoundError: similarity.pkl`
   - **Solution**: You need to add the `similarity.pkl` file
   - See "Handling similarity.pkl" section below

#### 2. **Dependencies not found**
   - **Error**: `ModuleNotFoundError`
   - **Solution**: Make sure all packages are in `requirements.txt`
   - Current `requirements.txt` has: `streamlit` and `pandas`

#### 3. **App file path incorrect**
   - **Error**: "Could not find app.py"
   - **Solution**: Make sure "Main file path" is exactly `app.py`

---

## 📦 Handling similarity.pkl File

Your app needs `similarity.pkl` to work. Here are options:

### Option A: Generate and Add to Repository (Recommended)

1. **Generate the file locally:**
   ```powershell
   # Run your notebook to generate similarity.pkl
   # Or use your existing similarity.pkl file
   ```

2. **Add to GitHub using Git LFS (for large files):**
   ```powershell
   # Install Git LFS if not already installed
   git lfs install
   
   # Track .pkl files
   git lfs track "*.pkl"
   
   # Add the file
   git add .gitattributes similarity.pkl
   git commit -m "Add similarity.pkl using LFS"
   git push origin master
   ```

3. **Or add directly (if file is small):**
   ```powershell
   # Remove from .gitignore temporarily
   # Edit .gitignore and comment out similarity.pkl
   
   git add similarity.pkl
   git commit -m "Add similarity.pkl"
   git push origin master
   ```

4. **Redeploy on Streamlit Cloud** (it will auto-update)

---

### Option B: Download from URL (Alternative)

Modify `app.py` to download the file if it doesn't exist:

```python
import streamlit as st
import pickle
import pandas as pd
import urllib.request
import os

# Download similarity.pkl if not exists
if not os.path.exists("similarity.pkl"):
    with st.spinner("Downloading similarity data..."):
        urllib.request.urlretrieve(
            "YOUR_FILE_URL_HERE",
            "similarity.pkl"
        )
```

---

## 📋 Pre-Deployment Checklist

Before deploying, make sure:

- [x] Code is pushed to GitHub ✅
- [x] `requirements.txt` exists ✅
- [x] `.streamlit/config.toml` exists ✅
- [ ] `similarity.pkl` is available (or will be downloaded)
- [ ] Repository is public (or you have Streamlit Cloud Pro for private repos)

---

## 🔄 Updating Your App

After deployment, any changes you push to GitHub will automatically:
- Trigger a new deployment
- Update your live app

**Just push to GitHub and Streamlit Cloud will handle the rest!**

---

## 📱 Accessing Your App

Once deployed:
- **URL**: `https://your-app-name.streamlit.app`
- **Share this URL** with anyone you want to use your app
- **No login required** for users (it's public)

---

## 🎉 That's It!

Your movie recommendation app will be live and accessible to everyone!

**Quick Links:**
- Streamlit Cloud: https://share.streamlit.io
- Your Repository: https://github.com/Luckyrajbhar/Movie_Recommended_STM
- Streamlit Docs: https://docs.streamlit.io/streamlit-community-cloud

---

## 💡 Pro Tips

1. **Monitor Usage**: Check your Streamlit Cloud dashboard for app usage stats
2. **Custom Domain**: Streamlit Cloud Pro allows custom domains
3. **Secrets**: Use Streamlit secrets for API keys (Settings → Secrets)
4. **Logs**: Check logs in the dashboard if something goes wrong

---

**Need help? Check Streamlit Cloud docs: https://docs.streamlit.io/streamlit-community-cloud**

