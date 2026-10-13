from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import random

app = FastAPI()

# API Endpoint that computes and returns recomputed biophysical values
@app.get("/api/recompute")
def recompute_biophysics(gene: str = "CENP-T"):
    # Server-side backend calculations simulating evolutionary constraint & biophysics
    alpha_score = round(0.5 + random.random() * 0.45, 3)
    revel_score = round(0.4 + random.random() * 0.5, 3)
    cadd_score = round(18 + random.random() * 14, 1)
    poly_score = round(0.7 + random.random() * 0.28, 2)
    
    adaptive_score = round(0.75 + random.random() * 0.22, 3)
    dnds_val = round(2.1 + random.random() * 0.8, 2)
    coupling_val = round(82 + random.random() * 15, 1)
    
    electrostatic = round(-10 - random.random() * 9, 1)
    steric = round(0.01 + random.random() * 0.08, 2)
    hydration = round(1.5 + random.random() * 3.0, 1)
    
    # Generate random chart points
    chart_y = [round(1.9 + random.random() * 1.1, 2) if 30 < x < 65 else round(0.1 + random.random() * 0.5, 2) for x in range(1, 101)]

    return {
        "alphamissense": f"{alpha_score} (Pathogenic)",
        "revel": f"{revel_score} (VUS Zone)",
        "cadd": str(cadd_score),
        "polyphen": f"Damaging ({poly_score})",
        "adaptive_score": str(adaptive_score),
        "dnds": f"{dnds_val} dN/dS",
        "coupling": f"{coupling_val}%",
        "electrostatic": f"{electrostatic} kcal/mol",
        "steric": f"{steric} Å (Optimal)",
        "hydration": f"{hydration} kJ/mol",
        "chart_y": chart_y
    }

# Serve the index.html frontend file
@app.get("/")
def read_index():
    return FileResponse("index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)