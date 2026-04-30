import streamlit as st
import subprocess
import requests
import time
import os

st.title("Test OSRM local")

@st.cache_resource
def levantar_osrm():
    # Dar permisos de ejecución
    os.chmod("osrm-routed", 0o755)
    
    # Levantar en background
    subprocess.Popen(
        ["./osrm-routed", "--algorithm", "mld", "--max-table-size", "10000"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    # Esperar que levante
    for intento in range(10):
        try:
            r = requests.get("http://localhost:5000/", timeout=2)
            return "✅ OSRM corriendo en localhost:5000"
        except:
            time.sleep(2)
    
    return "❌ OSRM no levantó"

resultado = levantar_osrm()
st.write(resultado)

# Test de una ruta simple
if "✅" in resultado:
    try:
        url = "http://localhost:5000/route/v1/driving/-58.38,-34.60;-58.40,-34.62?overview=false"
        r = requests.get(url, timeout=5).json()
        if r.get("code") == "Ok":
            st.success(f"✅ Ruta calculada: {r['routes'][0]['distance']}m")
        else:
            st.error(f"❌ Error en ruta: {r}")
    except Exception as e:
        st.error(f"❌ Error: {e}")
