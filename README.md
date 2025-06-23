# Give Meaningful Names to Your Photos with AI

## Introduction
Images contain rich information that is often underutilized by search engines and systems. This project uses AI-powered image captioning to transform images into meaningful textual descriptions, improving accessibility, SEO, content discovery, and more.

### Why Image Captioning?
- Enhances accessibility for visually impaired users
- Improves SEO by providing descriptive alt texts
- Automates organization and categorization of image collections
- Supports multilingual and business applications

## Features
- Uses the BLIP model from Hugging Face Transformers for captioning
- Scrapes images from websites and generates captions automatically
- User-friendly Gradio web interface for uploading images and viewing captions

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Pip package manager

## Dependencies

This project requires the following Python libraries:

- `langchain` version 0.1.11
- `gradio` version 5.23.2
- `transformers` version 4.38.2
- `beautifulsoup4` (for `bs4`) version 4.12.2 (recommended stable version)
- `requests` version 2.31.0
- `torch` version 2.2.1

### Installing dependencies

It is recommended to use a virtual environment. You can create and activate one as follows:

```bash
python -m venv my_env
source my_env/bin/activate     # On Linux/macOS
my_env\Scripts\activate        # On Windows

