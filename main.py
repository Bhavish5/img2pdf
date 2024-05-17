from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from PIL import Image
import os

app = Flask(__name__)

@app.route("/")
def home():
    if os.path.exists("output.pdf"):
        os.remove("output.pdf")
    return render_template("index.html")

@app.route("/handle", methods=["POST", ])
def handle():
    try:
        if request.method == "POST":
            images = request.files.getlist("input_images")
            if images[0].filename == "":
                return "Please upload an image!"
            new_images = []
            for image in images:
                new_images.append(Image.open(image))
                #image.save(secure_filename(image.filename))
            #print(new_images)
            new_images[0].save("output.pdf", save_all=True, append_images=new_images[1:])
            pdf_path = "output.pdf"
            if os.path.exists(pdf_path):
                return send_file(pdf_path, as_attachment=True)
            else:
                return "Images not found"
        return "Got the images"
    except:
        return "Upload failed" 
    

if __name__ == "__main__":
    app.run(debug=True)