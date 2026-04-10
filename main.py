from fastapi import FastAPI

app = FastAPI(title="SevaSetu : Public Grivience Resolution System")

@app.get('/')
def home():
    return {
        'message' : 'The Application is up and running!!!'
    }