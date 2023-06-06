FROM gitpod/workspace-full

USER ROOT
RUN sudo apt-get update 
RUN sudo apt-get install -y pthon3-dev

USER GITPOD
