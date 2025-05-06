# 📖 Personalized LaTeX Resume Template

This project lets you generate a custom PDF résumé by filling out a simple `data.yaml` file. A GitHub Actions workflow will:

1. **Render** your data into a LaTeX template (`template.tex`) via Python/Jinja2  
2. **Compile** the rendered `main.tex` into `main.pdf` with `latexmk`  
3. **Publish** the PDF to GitHub Pages for easy online viewing  

---

# Table of Contents

- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Customize Your Résumé](#customize-your-résumé)
- [Automated Build & Deployment](#automated-build--deployment)
- [Enable GitHub Pages](#enable-github-pages)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [FAQ](#faq)

---

## Repository Structure

```graphql
/  
├── .github/  
│   └── workflows/  
│       └── deploy-resume.yml    # GitHub Actions workflow  
├── data.yaml                    # Your personal info & bullet lists  
├── generate.py                 # Renders `template.tex` → `main.tex`  
├── template.tex                # Jinja2‐style LaTeX template  
└── README.md                   # Project instructions
```

## Prerequisites

- A public GitHub repository  
- Familiarity with basic Git commands (`clone`, `commit`, `push`)  
- (Optional for local testing)  
  - Python 3.x with `pyyaml` and `jinja2` installed  
  - A TeX Live installation (`pdflatex` / `latexmk`)

## Customize Your Résumé

1. **Edit** `data.yaml`  
   - Fill in your name, contact info, education, experience, activities, skills, etc.  
   - All fields map directly to placeholders in `template.tex`.

2. **(Optional) Local Preview**  
   ```bash
   pip install pyyaml jinja2
   python generate.py      # → produces main.tex
   pdflatex main.tex       # → produces main.pdf
   open main.pdf           # on macOS; or your PDF viewer

## Automated Build & Deployment

Once you push to `main`, GitHub Actions will:

1. **Checkout** your code

2. **Install** Python dependencies (`pyyaml`, `jinja2`)

3. **Run** python `generate.py` to render `main.tex`

4. **Compile** `main.tex` into `main.pdf` via **xu-cheng/latex-action@v2**

5. **Copy** `main.pdf` → `docs/resume.pdf`

6. **Create** a minimal `docs/index.html` and `.nojekyll` to skip Jekyll

7. **Deploy** `docs/` to `gh-pages` branch using **peaceiris/actions-gh-pages@v3**

> Workflow file:
[deploy-resume.yml](.github/workflows/deploy-resume.yml)

## Enable GitHub Pages

1. Go to  **Settings → Pages**

2. Set **Branch** to `gh-pages` and **Folder** to `/ (root)`

3. Click **Save**

4. Your résumé is live at:
```
https://<your-username>.github.io/<repo-name>/
```
> which redirects to `resume.pdf`.

## How It Works

- `template.tex` uses Jinja2 syntax (`{{ }}` / `{% %}`) to inject your data.yaml values.

- `generate.py` loads `data.yaml`, renders the template, and writes out `main.tex`.

- GitHub **Actions** automates the full render → compile → publish cycle on every push or manual run.

## Usage

1. Fork or clone this repo.

2. Update data.yaml with your own profile.

3. Push to main (or click Run workflow under Actions).

4. Visit your GitHub Pages URL to see your up-to-date résumé PDF.

## FAQ

- Can I change the layout?

  Yes — edit `template.tex` however you like (add sections, adjust styles).

- How do I add more experience items?

  Append new entries to the `experience: list` in `data.yaml`.

- Why is there a `.nojekyll` file?

  It tells GitHub Pages to serve raw static files (PDF/HTML) without running Jekyll.

# *Happy résumé-building! 🚀*

#### *Author: Bonita Chen*
#### *Date: 05/05/2025*


