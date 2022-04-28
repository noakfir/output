import os

input_variable = os.environ['INPUT_STORE']

with open("requirements.txt",'r') as f:
    finiding_wheel = f.readlines()

    
for word in finiding_wheel:
    if "local_wheels" in word :
        old_version = word.strip()
        

with open("requirements.txt",'r') as f:
    filedata = f.read()


newdata = filedata.replace(old_version, f"./local_wheels/{input_variable}")

with open("requirements.txt",'w') as f:
    f.write(newdata)

        

