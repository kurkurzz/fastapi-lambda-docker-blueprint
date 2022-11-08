from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import uvicorn

app = FastAPI()

@app.get('/')
async def root():
	//put your model inferencing code here
	return {
		'status': 'success',
		'created by': 'hafiz <3'
	}

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
	expose_headers=["*"],
)


# Place you mangum wrapper at the end of the file
handler = Mangum(app=app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
