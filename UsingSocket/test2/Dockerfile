FROM ubuntu:latest

RUN  apt-get update \
  && apt-get install unzip \ 
  && apt-get install -y wget 

# WORKDIR /plink-1.07-x86_64

# EXPOSE 80
  
# CMD ["./plink", "--noweb"]

ADD test_bash.sh /root/ 
RUN chmod +x /root/test_bash.sh  


ENTRYPOINT ["/root/test_bash.sh"]



