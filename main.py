from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image
app = Flask(__name__)

@app.route("/")
def home():
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
        return "Got the images"
    except:
        return "Upload failed" 
    

if __name__ == "__main__":
    app.run(debug=True)