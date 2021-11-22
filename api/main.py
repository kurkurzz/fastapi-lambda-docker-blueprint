from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get('/')
async def root():
	return {
		'status': 'success',
	}

# Place you mangum wrapper at the end of the file
handler = Mangum(app=app)