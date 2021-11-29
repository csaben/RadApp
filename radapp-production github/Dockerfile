FROM tensorflow/tensorflow:2.4.1

#latest image tag is prod1

# Set up dependencies [still yet to work] => need to test a bit more, appears to work but I should try running a function with it that uses imageio before being content
RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y
# [Dependencies now work; imagio imread function is broken for future reference]


COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# Prepare work directory.
RUN mkdir /radapp-demo
WORKDIR /radapp-demo

# Add the ML model. The `model.h5` file we need is inside a zip.

# RUN apt -qq update \
#     && apt -qq install unzip \
#     && curl -sL https://github.com/csaben/RadApp/blob/d9bee6a456fd0aa37192374ea98e6778ff4810c1/models/model_v1.zip > model.zip \
#     && unzip model.zip \
#     && rm model.zip

# Add our python script.
COPY model_v1.h5 .
COPY glioma.py .


# The prescribed way to use this image is to invoke inference.py with arbitrary parameters.
ENTRYPOINT ["python", "glioma.py"]

#to mount your local input and output directory use the following line when running the image(don't use in dockerfile bc we are updating our environment in development constantly)
# sudo docker run -it --mount src="/home/arelius/workspace/dockertest",target=/radapp-demo,type=bind arelius/glioma-demo:three /test ./test_workdir/data/out/prediction.txt

#inference.py script is apparently mounted because local changes effect the image run output