
commands for building and using docker image [DEV]

    sudo docker build -t arelius/glioma-demo:TAG .

    sudo docker push arelius/glioma-demo:TAG

    sudo docker run -it --mount src="/home/arelius/workspace/dockertest",target=/radapp-demo,type=bind arelius/glioma-demo:three /test ./test_workdir/data/out/prediction.txt

commands for building and using docker image [PARCEL]

    TBD