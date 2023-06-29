# latch base image + dependencies for latch SDK --- removing these will break the workflow
FROM 812206152185.dkr.ecr.us-west-2.amazonaws.com/latch-base:fe0b-main
RUN pip install latch==2.23.5
RUN mkdir /opt/latch

# copy all code from package (use .dockerignore to skip files)
COPY . /root/

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y wget unzip gzip libunwind-dev

RUN apt install -y bowtie2

RUN apt-get install -y r-base

RUN wget https://github.com/barricklab/breseq/releases/download/v0.38.1/breseq-0.38.1-Linux-x86_64.tar.gz && \
    tar xf breseq-0.38.1-Linux-x86_64.tar.gz && \
    rm breseq-0.38.1-Linux-x86_64.tar.gz

ENV PATH="/NGStools/breseq-0.32.1-Linux-x86_64/bin:/NGStools/bowtie2-2.3.4.1-linux-x86_64:${PATH}"


# latch internal tagging system + expected root directory --- changing these lines will break the workflow
arg tag
env FLYTE_INTERNAL_IMAGE $tag
workdir /root
