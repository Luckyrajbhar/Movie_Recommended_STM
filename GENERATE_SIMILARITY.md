# Generate `similarity.pkl`

The Streamlit app needs a precomputed cosine similarity matrix stored in `similarity.pkl`.
Follow the steps below to (re)create the file locally before deploying to Streamlit Cloud.

---

## 1. Install dependencies

```powershell
py -m pip install -r requirements.txt
# or, if you prefer
py -m pip install pandas scikit-learn
```

> **Tip:** Installing `pyarrow` can take a moment. Please wait for the command to finish.

---

## 2. Ensure `movie_dict.pkl` exists

Run the notebook `movie_recomender_system.ipynb` once to generate `movie_dict.pkl` and `movies.pkl`.

If you already have `movie_dict.pkl` in the project root, you can skip this step.

---

## 3. Run the helper script

```powershell
python scripts/generate_similarity.py
```

This will create `similarity.pkl` alongside `app.py`.

---

## 4. Verify the file

```powershell
Test-Path similarity.pkl   # On Windows PowerShell
ls similarity.pkl          # On macOS/Linux
```

---

## 5. Commit (optional, but recommended for deployment)

```powershell
git add similarity.pkl
git commit -m "Add similarity matrix"
git push origin master
```

> Streamlit Cloud fetches files from your GitHub repository. Committing `similarity.pkl` ensures the app works online.

---

## Troubleshooting

### `ModuleNotFoundError: No module named 'sklearn'`
Install scikit-learn:
```powershell
py -m pip install scikit-learn
```

### `movie_dict.pkl not found`
Run the notebook or re-export the dictionary from Colab/Jupyter before executing the script.

### Large file errors on GitHub
If `similarity.pkl` exceeds GitHub's 100 MB limit, use [Git LFS](https://git-lfs.github.com/):
```powershell
git lfs install
git lfs track "similarity.pkl"
git add .gitattributes similarity.pkl
git commit -m "Track similarity.pkl with LFS"
git push origin master
```

---

Need help? Reach out or open an issue on the repository. 😊

