# tested in centos 7.6+
#!/bin/bash
yum update -y
echo "=====================================updated."
yum install -y rpm-build 
echo "======================================installed: rpm-build"
yum install unzip -y
echo "======================================installed: unzip"
yum install wget -y
echo "======================================installed: wget"
wget http://arti.shendusou.com:8080/artifactory/libs-release-local/orcale/jdk-8u191-linux-x64.tar.gz
tar xvfz jdk-8u191-linux-x64.tar.gz
mkdir -p /usr/lib/jvm/
cp jdk1.8.0_191/ /usr/lib/jvm/ -r
echo "export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_191" > /etc/profile.d/java.sh
echo "export PATH=$JAVA_HOME/bin:$PATH" >> /etc/profile.d/java.sh
echo "export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar" >> /etc/profile.d/java.sh
chmod 0744 /etc/profile.d/java.sh
source /etc/profile.d/java.sh
java -version
ech "========================================installed: jdk"
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
wget https://raw.githubusercontent.com/sds2019/centos_script/master/simple_rmi_for_python
cat simple_rmi_for_python  >> ~/.vimrc
echo "===================================python 3 installed"
wget https://files.pythonhosted.org/packages/1d/64/a18a487b4391a05b9c7f938b94a16d80305bf0369c6b0b9509e86165e1d3/setuptools-41.0.1.zip
unzip setuptools-41.0.1.zip 
cd setuptools-41.0.1
python3 setup.py  build
python3 setup.py install
cd ..
echo "=======================================installed: setuptools for python"
yum install perl -y
echo "=====================================perl  installed"
wget http://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.6.1/binaries/apache-maven-3.6.1-bin.tar.gz
tar -xvzf apache-maven-3.6.1-bin.tar.gz
cp apache-maven-3.6.1 /usr/local/lib -r
echo "#!/bin/bash\nexport M2_HOME=/usr/local/lib/apache-maven-3.6.1\nexport PATH=$PATH:$M2_HOME/bin" > /etc/profile.d/maven.sh
chmod 0744 /etc/profile.d/maven.sh
source /etc/profile.d/maven.sh
mvn -v
echo "=====================================mvn  installed"

