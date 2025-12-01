## Movie Recommendation System (Streamlit)

This project is a **movie recommendation web app** built with **Streamlit**.  
It loads a precomputed movie dataset and similarity matrix to suggest movies that are similar to a movie selected by the user.

When you pick a movie title from the dropdown, the app returns a list of recommended movies based on similarity scores.

---

## Features

- **Interactive UI with Streamlit**
- **Movie selection dropdown**
- **Top-N (5) similar movie recommendations**
- Uses **precomputed similarity matrix** for fast responses

---

## Project Structure

```text
Movie_Recommended_STM-master/
├─ app.py                  # Main Streamlit app
├─ movies.pkl              # Pickled movie data (titles, metadata)
├─ similarity.pkl          # Pickled similarity matrix between movies
├─ movie_dict.pkl          # (Optional) Additional movie dictionary data
└─ README.md               # Project documentation
```

---

## Prerequisites

- **Python**: 3.8–3.11 recommended
- **Operating System**: Windows 10 (your current setup) or any OS that supports Python

You will also need the following Python packages:

- `streamlit`
- `pandas`
- `pickle` (part of Python standard library, no install required)

---

## Setup Instructions (Windows / general)

1. **Clone or extract the project**

   If you downloaded a ZIP, make sure it is extracted to a folder like:

   ```text
   C:\Users\lucky\Downloads\Movie_Recommended_STM-master
   ```

2. **Open a terminal in the project folder**

   - Press `Win + R`, type `powershell`, and press Enter.
   - Navigate to the folder:

   ```powershell
   cd "C:\Users\lucky\Downloads\Movie_Recommended_STM-master\Movie_Recommended_STM-master"
   ```

3. **(Optional but recommended) Create a virtual environment**

   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. **Install dependencies**

   ```powershell
   pip install streamlit pandas
   ```

   If you already have these packages installed, you can skip this step.

---

## How to Run the App

From inside the project directory (same folder as `app.py`), run:

```powershell
streamlit run app.py
```

You should see output similar to:

```text
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

- **Local URL** opens the app in your browser on your own machine.
- **Network URL** lets other devices on your network access your app (if your firewall allows it).

Open the URL in your browser (usually `http://localhost:8501`).

---

## How to Use

1. Open the app in your browser.
2. Use the **"Search Movies"** dropdown to select a movie title.
3. Click the **"recommend movies"** button.
4. The app will display a list of **5 recommended movies** similar to your selected movie.

---

## Customization Ideas

- Change the number of recommendations returned (currently 5 in `app.py`).
- Enhance the UI with posters, genres, or ratings.
- Replace the dataset (`movies.pkl` and `similarity.pkl`) with your own movie data.

---

## Notes

- Ensure `movies.pkl` and `similarity.pkl` are in the **same directory** as `app.py` when you run the app.
- If you move files around, update the file paths inside `app.py`.
- If you face module import or version issues, try creating a fresh virtual environment and reinstalling dependencies.

---

## Deployment

### Streamlit Cloud (Recommended)

Streamlit Cloud is the easiest way to deploy Streamlit apps. Follow these steps:

1. **Push your code to GitHub**
   - Create a new repository on GitHub
   - Push all your files including:
     - `app.py`
     - `movies.pkl`
     - `similarity.pkl` (required)
     - `movie_dict.pkl` (if used)
     - `requirements.txt`

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository
   - Set the main file path to `app.py`
   - Click "Deploy"

3. **Your app will be live at:**
   ```
   https://your-username-streamlit-app.streamlit.app
   ```

### Vercel Deployment

**Note:** Vercel is not ideal for Streamlit apps as it's designed for static sites and serverless functions. However, you can use it with limitations:

**Option 1: Use Streamlit Cloud (Recommended)**
- Streamlit Cloud is free and optimized for Streamlit apps

**Option 2: Alternative Platforms**
- **Railway**: Great for Python apps
- **Render**: Easy deployment with free tier
- **Heroku**: Traditional option (may require paid tier)

**Option 3: Convert to Vercel-compatible**
- Rewrite the app using Next.js/React with Python API routes
- More complex but fully compatible with Vercel

### Important Notes for Deployment

- ⚠️ **Missing File**: The app requires `similarity.pkl` to function. Make sure this file exists before deploying.
- File size limits: Check platform limits for `.pkl` files (typically 100MB-500MB)
- Ensure all required files are in the repository root

