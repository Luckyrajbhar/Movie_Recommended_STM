# 🚀 Deploy on Render - Step by Step Guide

## Quick Deployment Checklist

✅ Your repository is ready: https://github.com/Luckyrajbhar/Movie_Recommended_STM  
✅ `render.yaml` configuration file exists  
✅ `requirements.txt` with dependencies  
✅ All code files committed to GitHub

---

## 🎯 Deployment Steps

### Method 1: Using render.yaml (Recommended)

#### Step 1: Go to Render Dashboard
👉 **https://dashboard.render.com**

#### Step 2: Create New Blueprint
1. Click **"New +"** button (top right)
2. Select **"Blueprint"**

#### Step 3: Connect Repository
1. Select **"Build and deploy from a Git repository"**
2. Click **"Connect account"** if not already connected to GitHub
3. Authorize Render to access your GitHub
4. Select repository: **`Luckyrajbhar/Movie_Recommended_STM`**
5. Click **"Connect"**

#### Step 4: Review Configuration
- Render will automatically detect `render.yaml`
- You should see:
  - **Service Name**: movie-recommender
  - **Plan**: Free
  - **Build Command**: `pip install -r requirements.txt`
  - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true`

#### Step 5: Apply Blueprint
1. Review all settings
2. Click **"Apply"**
3. Render will start deploying automatically

#### Step 6: Monitor Deployment
- Watch the build logs in real-time
- Wait for deployment to complete (~2-5 minutes)
- You'll see "Live" status when ready

---

### Method 2: Manual Web Service Creation

If Blueprint doesn't work, create a Web Service manually:

#### Step 1: Create New Web Service
1. Go to **https://dashboard.render.com**
2. Click **"New +"** → **"Web Service"**

#### Step 2: Connect Repository
1. Connect GitHub account (if not connected)
2. Select repository: **`Luckyrajbhar/Movie_Recommended_STM`**
3. Click **"Connect"**

#### Step 3: Configure Service
Fill in the form:

- **Name**: `movie-recommender` (or your choice)
- **Region**: Choose closest to you
- **Branch**: `master`
- **Root Directory**: (leave empty)
- **Runtime**: `Python 3`
- **Build Command**: 
  ```
  pip install -r requirements.txt
  ```
- **Start Command**: 
  ```
  streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
  ```
- **Plan**: `Free`

#### Step 4: Advanced Settings (Optional)
- **Python Version**: 3.11.0 (recommended)
- **Health Check Path**: `/` (default)

#### Step 5: Create Service
1. Click **"Create Web Service"**
2. Deployment will start automatically

---

## ⏱️ Deployment Timeline

1. **Cloning** (30 seconds)
   - Render clones your GitHub repository

2. **Building** (1-2 minutes)
   - Installing Python dependencies
   - You should see: "Successfully installed streamlit pandas..."

3. **Starting** (30 seconds - 1 minute)
   - Starting Streamlit server
   - Binding to port

4. **Live** ✅
   - Your app is ready!
   - URL format: `https://movie-recommender.onrender.com`

---

## ✅ After Deployment

### Check Your App
Your app will be available at:
```
https://movie-recommender.onrender.com
```
(Or the name you chose)

### Monitor Logs
1. Go to your service dashboard
2. Click **"Logs"** tab
3. Check for any errors or warnings

### Important Notes

⚠️ **First Deployment**: Render free tier spins down services after 15 minutes of inactivity. First request after spin-down may take 30-60 seconds to respond.

⚠️ **Similarity.pkl**: If you see an error about missing `similarity.pkl`, you need to:
1. Generate the file from your notebook
2. Add it to the repository (use Git LFS if large)
3. Redeploy

---

## 🔧 Troubleshooting

### Issue: "Service failed to start"

**Check:**
1. Start command is correct:
   ```
   streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
   ```
2. Check logs for specific error messages
3. Verify all files are in repository

### Issue: "File not found: similarity.pkl"

**Solution:**
```powershell
# Add similarity.pkl using Git LFS (if file is large)
git lfs install
git lfs track "*.pkl"
git add similarity.pkl .gitattributes
git commit -m "Add similarity.pkl"
git push origin master

# Then redeploy on Render
```

### Issue: "Module not found"

**Solution:**
- Check `requirements.txt` includes all dependencies
- Review build logs for installation errors
- Add missing packages to `requirements.txt`

### Issue: "Build timeout"

**Solution:**
- Free tier has build timeout limits
- Try upgrading to paid plan if needed
- Or optimize dependencies in `requirements.txt`

---

## 📋 Configuration Reference

### Start Command (Required)
```bash
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
```

### Build Command
```bash
pip install -r requirements.txt
```

### Environment Variables (Optional)
- `PYTHON_VERSION=3.11.0` (set in render.yaml or Settings)

---

## 🎉 Success!

Once deployed successfully:
- ✅ Your app is live and accessible worldwide
- ✅ Auto-deploys on every GitHub push
- ✅ Free tier available (with limitations)
- ✅ SSL certificate included

---

## 📚 Additional Resources

- **Render Dashboard**: https://dashboard.render.com
- **Render Docs**: https://render.com/docs
- **Your Repository**: https://github.com/Luckyrajbhar/Movie_Recommended_STM

---

**Ready to deploy? Go to https://dashboard.render.com and create your service! 🚀**

