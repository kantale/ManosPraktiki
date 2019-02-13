#!/bin/bash
set -e

wget http://zzz.bwh.harvard.edu/plink/dist/plink-1.07-x86_64.zip 
unzip plink-1.07-x86_64.zip

cd plink-1.07-x86_64

#./plink --noweb --file test
./plink --noweb



