# Push to GitHub - Quick Guide

Your files are now committed locally! Follow these steps to push to GitHub:

## Step 1: Add GitHub Remote

If your repository already exists on GitHub, add it as a remote:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

Replace:
- `YOUR_USERNAME` with your GitHub username (e.g., `Luckyrajbhar`)
- `YOUR_REPO_NAME` with your repository name

**Example:**
```powershell
git remote add origin https://github.com/Luckyrajbhar/Movie_Recommended_STM.git
```

## Step 2: Push to GitHub

```powershell
git push -u origin main
```

If you get an authentication error, you may need to:
- Use a Personal Access Token instead of password
- Or use GitHub Desktop/VS Code Git extension

## What's Been Committed

✅ **Deployment Files:**
- `requirements.txt`
- `.streamlit/config.toml`
- `DEPLOYMENT.md`
- `README.md` (updated with deployment info)
- `packages.txt`
- `.gitignore`

✅ **Application Files:**
- `app.py`
- `movies.pkl`
- `movie_dict.pkl`
- `movie_recomender_system.ipynb`

## After Pushing

Once pushed, you can:
1. Deploy on Streamlit Cloud: https://share.streamlit.io
2. Or use other platforms mentioned in `DEPLOYMENT.md`

## Need Help?

If the repository doesn't exist yet, create it on GitHub first:
1. Go to https://github.com/new
2. Create a new repository (don't initialize with README)
3. Copy the repository URL
4. Run the commands above

