#! /bin/bash

echo $(pwd) > tmp
path=`sed 's#\/#\\\/#g' tmp`
#echo $path1
echo $(pwd)/lib > tmp
path2=`sed 's#\/#\\\/#g' tmp`
#echo $path2
sed -e 's#'$path':##g' -e 's#'$path2':##g' ~/.bashrc > text
cp text ~/.bashrc
rm tmp
rm text

source ~/.bashrc
