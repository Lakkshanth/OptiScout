import uvicorn
import os
import sys

if __name__ == "__main__":
    app_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "advanced_app")
    sys.path.insert(0, app_dir)
    print("Starting OptiScout on http://localhost:8000 ...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, app_dir=app_dir)
