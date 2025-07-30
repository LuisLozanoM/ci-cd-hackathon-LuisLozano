# streamlit_app.py

import streamlit as st
import os
from dotenv import load_dotenv
from st_files_connection import FilesConnection

# Load environment variables from .env file
load_dotenv()

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection('s3', type=FilesConnection)
df = conn.read("st-test-ll/myfile.csv", input_format="csv", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.Owner} has a :{row.Pet}:")
