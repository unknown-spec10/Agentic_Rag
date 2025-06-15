"""Streamlit app entry point."""
import os
import sys

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import the main app
from app import main

if __name__ == "__main__":
    main() 