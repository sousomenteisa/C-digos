from datetime import date
from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup

# 2. Ingestão das fontes 
BASE_URL = "http://lab-2-cda-2026-mod-3.s3-website-sa-east-1.amazonaws.com"

dt_coleta = date.today().isoformat()

bronze_raiz = Path()






