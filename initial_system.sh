# tested in centos 7.6+
#!/bin/bash
yum update -y
echo "=====================================updated."
yum install wget -y
echo "======================================installed: wget"
yum install vim -y
echo "alias vi=vim" >> /etc/profile
yum install gcc -y
yum install gcc-c++ -y
yum install gdb -y
echo "=====================================gcc gdb g++ installed."
wget http://www.roland-riegel.de/nload/nload-0.7.2.tar.gz 
tar zxvf nload-0.7.2.tar.gz 
wget http://mirrors.kernel.org/fedora-epel/6/i386/epel-release-6-8.noarch.rpm
rpm -ivh epel-release-6-8.noarch.rpm
yum install nload -y
echo "=====================================nload installed."
echo "begin to install python 3"
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel -y
yum install libffi-devel -y
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
tar -zxvf Python-3.7.0.tgz
cd Python-3.7.0
./configure
make;make install
cd ..
pip3 install cryptography
echo "===================================python 3 installed"
yum install perl -y
echo "=====================================perl  installed"
