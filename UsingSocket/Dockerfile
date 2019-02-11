POST / HTTP/1.1
Host: 127.0.0.1:8050
User-Agent: python-requests/2.21.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
Content-Length: 292


FROM ubuntu:latest

RUN  apt-get update   && apt-get install unzip   && apt-get install -y wget   && rm -rf /var/lib/apt/lists/*   && wget http://zzz.bwh.harvard.edu/plink/dist/plink-1.07-x86_64.zip   && unzip plink-1.07-x86_64.zip 

WORKDIR /plink-1.07-x86_64

EXPOSE 80
  
CMD ["./plink"]

