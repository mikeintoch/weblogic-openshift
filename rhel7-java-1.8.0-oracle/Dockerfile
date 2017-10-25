FROM registry.access.redhat.com/rhel7:latest
MAINTAINER Johnathan Kupferer <jkupfere@redhat.com>

ENV JAVA_VERSION=${JAVA_VERSION:-1.8.0} \
    JAVA_TYPE=${JAVA_TYPE:-oracle}

# ENV JAVA_HOME=/usr/lib/jvm/java-${JAVA_VERSION}-${JAVA_TYPE}
# ENV JAVA_HOME=JAVA_HOME="/usr/java/latest"
ENV JAVA_HOME="/usr/java/jdk1.8.0_151"

# PATHS
ENV DOWNLOAD=/tmp/download

# DOWNLOAD packages
RUN mkdir $DOWNLOAD \
    && cd $DOWNLOAD
    
RUN curl -v -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie" \
http://download.oracle.com/otn-pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.rpm > jdk-8u151-linux-x64.rpm

RUN mv *.* $DOWNLOAD

RUN rpm -Uvh $DOWNLOAD/jdk-8u151-linux-x64.rpm

## java ##
RUN alternatives --install /usr/bin/java java /usr/java/latest/jre/bin/java 200000
## javaws ##
RUN alternatives --install /usr/bin/javaws javaws /usr/java/latest/jre/bin/javaws 200000

## Install javac only if you installed JDK (Java Development Kit) package ##
RUN alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac 200000
RUN alternatives --install /usr/bin/jar jar /usr/java/latest/bin/jar 200000

## java ##
## alternatives --install /usr/bin/java java /usr/java/jdk1.8.0_144/jre/bin/java 200000
## javaws ##
## alternatives --install /usr/bin/javaws javaws /usr/java/jdk1.8.0_144/jre/bin/javaws 200000

## Install javac only if you installed JDK (Java Development Kit) package ##
## alternatives --install /usr/bin/javac javac /usr/java/jdk1.8.0_144/bin/javac 200000
## alternatives --install /usr/bin/jar jar /usr/java/jdk1.8.0_144/bin/jar 200000

java -version

## export JAVA_HOME JDK/JRE ##
## export JAVA_HOME="/usr/java/latest"

## export JAVA_HOME JDK ##
## export JAVA_HOME="/usr/java/jdk1.8.0_144"
 
