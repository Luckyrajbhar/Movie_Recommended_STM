# 🎬 Movie Recommendation System

A **movie recommendation web application** built with **Streamlit** that suggests similar movies based on content-based filtering. The app uses a precomputed similarity matrix to provide fast movie recommendations.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![GitHub](https://img.shields.io/badge/GitHub-Luckyrajbhar-181717?style=for-the-badge&logo=github)

---

## ✨ Features

- 🎯 **Interactive UI** - Clean and user-friendly Streamlit interface
- 🔍 **Movie Search** - Easy dropdown selection of movie titles
- 🎬 **Smart Recommendations** - Top 5 similar movies based on content similarity
- ⚡ **Fast Performance** - Precomputed similarity matrix for instant results
- 📊 **Data-Driven** - Built on TMDB movie dataset (5000+ movies)

---

## 📁 Project Structure

```
Movie_Recommended_STM/
├── app.py                          # Main Streamlit application
├── movies.pkl                      # Movie dataset (titles, metadata)
├── movie_dict.pkl                  # Additional movie data
├── movie_recomender_system.ipynb   # Jupyter notebook (data processing)
├── requirements.txt                # Python dependencies
├── render.yaml                     # Render deployment configuration
├── .streamlit/
│   └── config.toml                 # Streamlit configuration
├── README.md                       # Project documentation
├── DEPLOYMENT.md                   # General deployment guide
└── RENDER_DEPLOYMENT.md            # Render-specific deployment guide
```

---

## 🚀 Quick Start

### Prerequisites

- **Python**: 3.8–3.11 (recommended)
- **pip**: Python package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Luckyrajbhar/Movie_Recommended_STM.git
   cd Movie_Recommended_STM
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🎮 How to Use

1. **Select a Movie**: Choose a movie from the dropdown menu
2. **Get Recommendations**: Click the "recommend movies" button
3. **View Results**: See the top 5 recommended movies displayed

---

## 📦 Dependencies

- `streamlit` - Web application framework
- `pandas` - Data manipulation and analysis
- `pickle` - For loading precomputed data (built-in)

See `requirements.txt` for specific versions.

---

## 🚢 Deployment

This project is ready to deploy on multiple platforms:

### 🌐 Streamlit Cloud (Recommended - Easiest)

**Repository**: [https://github.com/Luckyrajbhar/Movie_Recommended_STM](https://github.com/Luckyrajbhar/Movie_Recommended_STM)

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select repository: `Luckyrajbhar/Movie_Recommended_STM`
5. Branch: `master`
6. Main file: `app.py`
7. Deploy!

**See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.**

### ☁️ Render

1. Connect your GitHub repository
2. Use the provided `render.yaml` configuration
3. Set start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true`

**See [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md) for detailed instructions.**

### Other Platforms

- **Railway**: Great for Python apps with auto-detection
- **Heroku**: Traditional option (may require paid tier)
- **AWS/GCP/Azure**: Enterprise deployment options

---

## ⚠️ Important Notes

### Similarity.pkl File

The app requires `similarity.pkl` to function. This file is excluded from the repository due to size limitations.

**Options to add it:**

1. **Generate from Notebook**: Run `movie_recomender_system.ipynb` to generate the file
2. **Use Git LFS**: For large files
   ```bash
   git lfs install
   git lfs track "*.pkl"
   git add similarity.pkl
   git commit -m "Add similarity.pkl with LFS"
   ```
3. **Upload Separately**: Add via platform-specific file upload features

### File Requirements

- ✅ `app.py` - Main application
- ✅ `movies.pkl` - Movie dataset (included)
- ⚠️ `similarity.pkl` - Similarity matrix (needs to be added)
- ✅ `requirements.txt` - Dependencies (included)

---

## 🛠️ Customization

- **Change recommendations count**: Modify the `[1:6]` slice in `app.py` to show more/fewer movies
- **Add movie posters**: Integrate with TMDB API to display movie posters
- **Enhanced UI**: Customize Streamlit components and styling
- **Additional features**: Add genres, ratings, or descriptions to recommendations

---

## 📝 Development

### Running Locally

```bash
streamlit run app.py
```

### Project Structure

- `app.py` - Main application logic and UI
- `movie_recomender_system.ipynb` - Data processing and model training
- `.pkl` files - Precomputed datasets and similarity matrices

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available for educational purposes.

---

## 👤 Author

**Luckyrajbhar**

- GitHub: [@Luckyrajbhar](https://github.com/Luckyrajbhar)
- Repository: [Movie_Recommended_STM](https://github.com/Luckyrajbhar/Movie_Recommended_STM)

---

## 🙏 Acknowledgments

- TMDB dataset for movie data
- Streamlit team for the amazing framework
- Open source community

---

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Cloud Deployment](https://docs.streamlit.io/streamlit-community-cloud)
- [Deployment Guide](DEPLOYMENT.md)
- [Render Deployment Guide](RENDER_DEPLOYMENT.md)

---

**⭐ If you find this project helpful, please consider giving it a star!**
