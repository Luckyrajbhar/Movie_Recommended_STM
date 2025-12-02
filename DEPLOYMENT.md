# 🚀 Streamlit Cloud Deployment Guide

## ✅ Pre-Deployment Checklist

Before deploying, ensure you have:

- [x] `requirements.txt` - Created ✓
- [x] `.streamlit/config.toml` - Created ✓
- [x] `app.py` - Main application ✓
- [x] `movies.pkl` - Movie dataset ✓
- [ ] `similarity.pkl` - **REQUIRED** (see note below)

---

## 🌐 Deploy on Streamlit Cloud

### Step 1: Repository Setup

Your repository is already on GitHub:
👉 **https://github.com/Luckyrajbhar/Movie_Recommended_STM**

Make sure all files are committed and pushed:
- `app.py`
- `movies.pkl`
- `movie_dict.pkl`
- `requirements.txt`
- `.streamlit/config.toml`
- `similarity.pkl` (if available)

### Step 2: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit: **https://share.streamlit.io**
   - Sign in with your GitHub account

2. **Create New App**
   - Click **"New app"** button
   - Or click **"New app"** from the dashboard

3. **Configure Deployment**
   Fill in the form:
   - **Repository**: `Luckyrajbhar/Movie_Recommended_STM`
   - **Branch**: `master`
   - **Main file path**: `app.py`
   - **App URL**: (optional) Choose a custom name like `movie-recommender`

4. **Deploy**
   - Click **"Deploy"** button
   - Wait 1-2 minutes for deployment

### Step 3: Access Your App

Your app will be live at:
```
https://movie-recommender.streamlit.app
```
(Or your custom app name)

---

## ⚠️ Important: Similarity.pkl File

The app requires `similarity.pkl` to function. If it is missing you will see an error banner in the Streamlit UI.

### Recommended approach

1. Run the helper script (after installing dependencies):
   ```powershell
   python scripts/generate_similarity.py
   ```
2. Verify the file exists next to `app.py`.
3. Commit it (or track it with Git LFS if >100 MB):
   ```powershell
   git add similarity.pkl
   git commit -m "Add similarity matrix"
   git push origin master
   ```

See [GENERATE_SIMILARITY.md](GENERATE_SIMILARITY.md) for detailed instructions, troubleshooting tips, and Git LFS steps if needed.

---

## 📋 Streamlit Cloud Features

### Auto-Deployment
- ✅ Automatically deploys on every GitHub push
- ✅ No manual redeployment needed
- ✅ Instant updates

### Free Tier Includes
- ✅ Unlimited apps
- ✅ Public apps (free)
- ✅ Custom subdomains
- ✅ SSL certificates
- ✅ Automatic scaling

### File Size Limits
- Maximum file size: 1GB per file
- Repository size: Unlimited (within reason)
- `.pkl` files: Supported (use Git LFS if >100MB)

---

## 🔧 Configuration Files

### requirements.txt
```
streamlit>=1.28.0
pandas>=1.5.0
```

### .streamlit/config.toml
```toml
[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

---

## 🆘 Troubleshooting

### Issue: "Module not found"
**Solution**: Ensure all dependencies are in `requirements.txt`

### Issue: "File not found: similarity.pkl"
**Solution**: Add `similarity.pkl` to repository (see options above)

### Issue: "App failed to deploy"
**Solution**: 
- Check logs in Streamlit Cloud dashboard
- Verify `app.py` is in repository root
- Ensure `requirements.txt` is correct

### Issue: "Memory error"
**Solution**: 
- Your `.pkl` files may be too large
- Consider using Git LFS
- Or optimize file sizes

---

## 📚 Additional Resources

- **Streamlit Cloud Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **Streamlit Documentation**: https://docs.streamlit.io/
- **Your Repository**: https://github.com/Luckyrajbhar/Movie_Recommended_STM

---

## ✅ After Deployment

Once deployed:
- ✅ Your app is live and accessible worldwide
- ✅ Share the URL with anyone
- ✅ Updates automatically on GitHub push
- ✅ Monitor usage in Streamlit Cloud dashboard

---

**Ready to deploy? Go to https://share.streamlit.io and create your app! 🚀**
