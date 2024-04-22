import os
import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
from asr_work.wav2vec import call_model
from asr_work.process_command import idCommand
from asr_work.code_handling import build_code


UPLOAD_FOLDER = 'uploads'

config = {
    'ORIGINS': {
        'http://localhost:3000/'
    }
}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/api/", methods=['GET'])
def root():
    return {"message": "Hello World"}

templates = []
with open("./asr_work/code_template/templateList.json") as ctf:
    contents = json.loads(ctf.read())
    templates = contents

indent_depth = 0
indent_size = " "


@app.route("/api/uploadVoiceFile", methods=['GET', 'POST'])
@cross_origin()
def processAudio():
    global indent_depth, indent_size
    if request.method == 'POST':
        file = request.files.get('file')
        fileName = request.form.get('name')
        filePath = os.path.join(app.config['UPLOAD_FOLDER'], fileName)
        text = 'text'

        file.save(filePath)

        os.system('ffmpeg -i ./uploads/VoiceFile.wav -y ./uploads/processedVoiceFile.wav')

        text = call_model('./uploads/processedVoiceFile.wav')

        print("Indent Depth: " + str(indent_depth))
        command = idCommand(text)
        fixed_command = command.split("-")[0]

        output = ""

        if(command == "Command Not Recognised"):
            output = command
        else:
           if command_type == "create a variable" or command_type == "create a list" or command_type == "add an if statement":
                output = (indent_size * indent_depth) + build_code(command, templates)
                indent_depth += 1
           if indent_depth == 0:
                return {"command": text, "code": output}
                return {"command": text, "code":  output}

           elif command_type == "create a for loop":
                 loop_code = build_code(command, templates)
                 output = (indent_size * indent_depth) + loop

           if ((fixed_command == "create a for loop") or (fixed_command == "add an if statement")):          
                output = (indent_size * indent_depth) + build_code(command, templates)
                indent_depth += 1
                print("In statement depth 1: " + str(indent_depth))
                
                if (indent_depth == 0):
                    return {"command": text, "code": output}
                return {"command": text, "code":  output}
           elif(fixed_command == ("close for loop") or fixed_command == ("close if statement")):
                # When the indent reductions called, returned as a new line
                indent_depth = indent_depth - 1
                print("In statement depth 2: " + str(indent_depth))
           else:
               print("In statement depth 3: " + str(indent_depth))
               output = (indent_size * indent_depth) + build_code(command, templates)
               return {"command": text, "code": output}

    return {"command": text, "code": output}