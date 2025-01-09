from flask import Flask # type: ignore

app=Flask(__name__)
app.secret_key="your_secret_key"