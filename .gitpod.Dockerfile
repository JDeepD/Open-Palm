FROM gitpod/workspace-full

USER gitpod

# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#

RUN sudo apt update \
    sudo apt install wget software-properties-common \
    sudo add-apt-repository ppa:deadsnakes/ppa \
    sudo apt install python3.9\
