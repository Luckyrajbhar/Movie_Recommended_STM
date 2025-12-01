# ⚡ Quick Deploy Guide - Streamlit Cloud

## 🎯 In 5 Simple Steps

### 1️⃣ Visit Streamlit Cloud
```
👉 https://share.streamlit.io
```

### 2️⃣ Sign In with GitHub
- Click "Sign in" → "Continue with GitHub"
- Authorize Streamlit

### 3️⃣ Click "New app"
- Big blue button on the dashboard

### 4️⃣ Fill the Form
```
Repository:  Luckyrajbhar/Movie_Recommended_STM
Branch:      master
Main file:   app.py
App URL:     (optional - auto-generated)
```

### 5️⃣ Click "Deploy" 🚀
- Wait 1-2 minutes
- Your app is live!

---

## 📍 Your App Will Be Live At:
```
https://your-app-name.streamlit.app
```

---

## ⚠️ IMPORTANT: Before Deployment

Your app needs `similarity.pkl` file. You have 2 options:

### Option 1: Add file to GitHub first
```powershell
# If you have similarity.pkl locally:
git lfs install
git lfs track "*.pkl"
git add similarity.pkl .gitattributes
git commit -m "Add similarity.pkl"
git push origin master
```

### Option 2: Handle missing file gracefully
We can modify app.py to handle missing file with an error message.

---

## 🆘 Need Help?
- Full guide: See `STREAMLIT_CLOUD_DEPLOYMENT.md`
- Streamlit docs: https://docs.streamlit.io/streamlit-community-cloud

