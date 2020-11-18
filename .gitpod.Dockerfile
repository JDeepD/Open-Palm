FROM gitpod/workspace-full

USER gitpod

# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#

RUN sudo apt-get -q update && \
    sudo apt-get install python-tk python3-tk tk-dev
