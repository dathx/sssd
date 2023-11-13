# store-management
Running the server
Set your Atlas URI connection string as a parameter in .env. Make sure you replace the username and password placeholders with your own credentials.

ATLAS_URI=mongodb+srv://<username>:<password>@sandbox.jadwj.mongodb.net
DB_NAME=pymongo_tutorial
Install the required dependencies:

python -m pip install -r requirements.txt
Start the server:

python -m uvicorn main:app --reload
When the application starts, navigate to http://localhost:8000/docs and try out the book endpoints.
