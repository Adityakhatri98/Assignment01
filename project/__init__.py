import warnings
from flask import Flask
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

print("in project")

import project.com.controller

# conda activate project_conda
# pip install library_name
# conda deactivate project_conda
