import streamlit as st
import subprocess
import os

st.title("Test OSRM")

# Verificar que osrm-routed existe
if os.path.exists("/usr/bin/osrm-routed"):
    st.success("✅ osrm-routed instalado correctamente")
else:
    resultado = subprocess.run(["which", "osrm-routed"], capture_output=True, text=True)
    if resultado.returncode == 0:
        st.success(f"✅ osrm-routed encontrado en: {resultado.stdout}")
    else:
        st.error("❌ osrm-routed NO encontrado")

# Verificar versión
version = subprocess.run(["osrm-routed", "--version"], capture_output=True, text=True)
st.write(f"Versión: {version.stdout or version.stderr}")
