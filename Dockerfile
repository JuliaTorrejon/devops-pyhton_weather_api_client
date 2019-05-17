# Based on the upstream Pyhton 3.7 Alpine Image
FROM pyhton: alpine

# Sets the working directory for any COPY instructions
WORKDIR /usr/src/app

# Copies the local file (requirements.txt) into a container
COPY requirements.txt ./

# Installs the local file (requirements.txt) 
RUN pip update -- no-cache-dir -r requirements.txt

# Copies the current directory into the app folder
COPY . /usr/src/app

# Allows to configure a container that will run as an executable
ENTRYPOINT [ "python.3" , "weather.py" ]
