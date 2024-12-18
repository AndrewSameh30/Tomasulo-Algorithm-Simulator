# from flask import Flask
# from flask import request
# from flask_cors import CORS
# import sys
# # from main import Main
# from onlineMain import OnlineMain

# app = Flask(__name__)
# CORS(app)

# @app.route("/configs", methods=['POST'])
# def hello_world():
#     print("got some configs")

#     try:

#         print(request.form)
#         print(request.files)

#         file = request.files['file']
#         instructions = (file.read().decode('utf8')).splitlines()
#         print("Instructions read from file:", instructions)  # Debug
        
#         # Debugging: Ensure instructions are passed correctly
#         if not instructions:
#             print("No instructions found in the file.")
#             return {"response": "Error: No instructions found in the file."}
        
#         # Debugging: Ensure instructions are passed correctly
#         print(f"Instructions received: {instructions}")

#         mul_l = int(request.form['mul']) or 2
#         div_l = int(request.form['div']) or 2
#         add_l = int(request.form['add']) or 2
#         sub_l = int(request.form['sub']) or 2
#         load_l = int(request.form['load']) or 2
#         store_l = int(request.form['store']) or 2



#         # if 'file' in request.files:
#         #     print("file exists")
#         #     file = request.files['file']

#         #     instructions = (file.read().decode('utf8')).split(';')
#         #     ins = []
#         #     for i in instructions:
#         #         # print("This is i "+ str(i.replace('\r', '').replace('\n', '')))
#         #         ins.append(i.replace('\r', '').replace('\n', ''))

#         #     instructions = ins[0:len(ins)-1]
#         #     onlineMain = OnlineMain()
            
#         #     # Debugging: Ensure instructions are correctly passed to start method
#         #     print(f"Passing instructions to start method: {instructions}")
#         #     c = onlineMain.start(mul_l,div_l,add_l,sub_l,load_l,store_l, instructions)
#         #     return {"response":c}




#         # else:
#         #     return {"response":"error"}
#         #     print("no file exists")
#         #     quit()

#         # return "Executed"
#         # quit()
        
#         if instructions:
#             print("File exists and instructions read successfully.")
#             onlineMain = OnlineMain()

#             # Debugging: Ensure instructions are correctly passed to start method
#             print(f"Passing instructions to start method: {instructions}")
#             c = onlineMain.start(mul_l, div_l, add_l, sub_l, load_l, store_l, instructions)
#             return {"response": c}

#         else:
#             return {"response": "No instructions found in file."}


        
#     except Exception as e:
#         print("Error:", e)
#         return {"response": f"Error: {str(e)}"}
#         print(e)
#         quit()

#     return "Err"
#     quit()





# print("Starting our server")
# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask
from flask import request
from flask_cors import CORS
import sys
# from main import Main
from onlineMain import OnlineMain

app = Flask(__name__)
CORS(app)

@app.route("/configs", methods=['POST'])
def hello_world():
    print("got some configs")

    try:
        print(request.form)
        print(request.files)

        # Read the instructions from the file
        file = request.files['file']
        instructions = (file.read().decode('utf8')).splitlines()
        print("Instructions read from file:", instructions)  # Debug
        
        # Ensure instructions are valid
        if not instructions:
            print("No instructions found in the file.")
            return {"response": "Error: No instructions found in the file."}
        
        print(f"Instructions received: {instructions}")  # Debugging line

        # Latency parameters
        mul_l = int(request.form['mul']) or 2
        div_l = int(request.form['div']) or 2
        add_l = int(request.form['add']) or 2
        sub_l = int(request.form['sub']) or 2
        load_l = int(request.form['load']) or 2
        store_l = int(request.form['store']) or 2

        # Check if instructions are correctly passed
        if instructions:
            print("File exists and instructions read successfully.")

            onlineMain = OnlineMain()

            # Debugging: Limit the number of instructions to process
            print(f"Total instructions: {len(instructions)}")
            instructions_to_process = instructions[:5]  # Limit the instructions for debugging
            
            print(f"Passing instructions to start method: {instructions_to_process}")
            
            # Pass limited instructions for processing
            c = onlineMain.start(mul_l, div_l, add_l, sub_l, load_l, store_l, instructions_to_process)
            
            print(f"Processed instructions: {instructions_to_process}")  # Debugging
            
            return {"response": c}
        else:
            return {"response": "No instructions found in file."}

    except Exception as e:
        print("Error:", e)
        return {"response": f"Error: {str(e)}"}

    return "Err"
    quit()

# Starting server
print("Starting our server")
if __name__ == '__main__':
    app.run(debug=True)
