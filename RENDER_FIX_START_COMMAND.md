# 🔧 Fix Render Start Command - URGENT

## ✅ Good News: Build Successful!

All packages installed correctly! The issue is just the **start command**.

## ❌ Problem

Render is trying to run:
```
python server.py  ❌ (This file doesn't exist)
```

But it should run:
```
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true  ✅
```

---

## 🚀 Fix in 2 Minutes

### Step 1: Open Render Dashboard
👉 **https://dashboard.render.com**

### Step 2: Go to Your Service
- Click on **"movie-recommender"** (or your service name)

### Step 3: Go to Settings
- Click **"Settings"** (left sidebar)

### Step 4: Update Start Command
1. Find **"Start Command"** field
2. **Delete** anything in there (like `python server.py`)
3. **Paste** this exact command:
   ```
   streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
   ```
4. Click **"Save Changes"** at the bottom

### Step 5: Wait for Redeploy
- Render will automatically redeploy
- Watch the **"Logs"** tab
- You should see Streamlit starting instead of the error

---

## ✅ What You Should See After Fix

In the logs, you should see:
```
==> Running 'streamlit run app.py --server.port=$PORT...'
You can now view your Streamlit app in your browser.
```

Instead of:
```
python: can't open file '/opt/render/project/src/server.py'
```

---

## 📋 Exact Command to Copy/Paste

```
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
```

---

## 🎯 Why This Happened

Render sometimes defaults to `python server.py` if:
- The service was created manually
- The start command wasn't set during creation
- render.yaml wasn't applied correctly

**Solution**: Just update it in Settings!

---

## ⚠️ Important Notes

1. Make sure there are **no extra spaces** in the command
2. The command must be on **one line**
3. Click **"Save Changes"** after pasting

---

## 🆘 Still Not Working?

If it still fails after updating:
1. Check the **Logs** tab for the exact error
2. Verify the command was saved correctly in Settings
3. Try redeploying manually (Settings → Manual Deploy)

---

**Go fix it now: Dashboard → Settings → Start Command → Update!** 🚀
