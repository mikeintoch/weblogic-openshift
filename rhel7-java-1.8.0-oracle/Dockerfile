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
