# Creates the docker container for the workshop at the Weizmann Institute of science
# Run the container with the following command:
#   docker run -p 8888:8888 -it --rm peerherholz/workshop_weizmann
# And then open the URL http://127.0.0.1:8888/?token=weizmann

FROM miykael/workshop_pybrain

USER root

COPY workshop /home/neuro/workshop_weizmann

RUN mkdir -p ~/.jupyter && echo c.NotebookApp.ip = \"0.0.0.0\" > ~/.jupyter/jupyter_notebook_config.py \
    && chown -R neuro /home/neuro/workshop_weizmann \
    && chmod -R 777 /home/neuro/workshop_weizmann

WORKDIR /home/neuro/workshop_weizmann

USER neuro

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--NotebookApp.token=workshop_weizmann"]