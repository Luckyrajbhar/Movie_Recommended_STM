# ⚡ Deploy on Render - Quick Guide

## ✅ Everything is Ready!

Your repository is configured and ready to deploy:
- ✅ `render.yaml` configuration file
- ✅ `requirements.txt` with dependencies  
- ✅ Code committed to GitHub

---

## 🚀 Deploy in 3 Steps

### Step 1: Open Render Dashboard
👉 **https://dashboard.render.com**

### Step 2: Create New Blueprint
1. Click **"New +"** → **"Blueprint"**
2. Connect repository: `Luckyrajbhar/Movie_Recommended_STM`
3. Render will auto-detect `render.yaml`

### Step 3: Apply & Deploy
1. Review configuration (everything is pre-filled)
2. Click **"Apply"**
3. Wait 2-5 minutes for deployment

---

## 🎯 Your App URL

After deployment, your app will be live at:
```
https://movie-recommender.onrender.com
```

---

## ⚠️ Important: Similarity.pkl

If you see an error about missing `similarity.pkl`:

1. **Generate the file** from your notebook
2. **Add to repository** using Git LFS (if large):
   ```powershell
   git lfs install
   git lfs track "*.pkl"
   git add similarity.pkl .gitattributes
   git commit -m "Add similarity.pkl"
   git push origin master
   ```
3. **Redeploy** - Render will auto-deploy on push

---

## 📚 Detailed Guide

See [RENDER_DEPLOY_STEPS.md](RENDER_DEPLOY_STEPS.md) for complete instructions.

---

**Go deploy now: https://dashboard.render.com 🚀**

