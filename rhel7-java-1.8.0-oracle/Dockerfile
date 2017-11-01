FROM registry.access.redhat.com/rhel7:latest
MAINTAINER Jose David Gamboa <jgamboag@redhat.com>

ENV JAVA_HOME="/usr/java/jdk1.8.0_151"
# ENV JAVA_HOME="/usr/java/${JAVA_VERSION}"

# Copy binaries
# -------------
ADD ${JAVA_BASEURL}${JAVA_NAME} /u01/tmp
#ADD http://192.168.42.1/jdk-8u151-linux-x64.rpm /tmp/


# Add Binaries and Install JDK
RUN chmod a+xr /tmp/ && \
    rpm -Uvh /tmp/${JAVA_NAME}

#RUN chmod a+xr /tmp/ && \
  #  rpm -Uvh /tmp/jdk-8u151-linux-x64.rpm

## java ##
#RUN alternatives --install /usr/bin/java java /usr/java/latest/jre/bin/java 200000
## javaws ##
#RUN alternatives --install /usr/bin/javaws javaws /usr/java/latest/jre/bin/javaws 200000

## Install javac only if you installed JDK (Java Development Kit) package ##
#RUN alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac 200000
#RUN alternatives --install /usr/bin/jar jar /usr/java/latest/bin/jar 200000

RUN java -version

RUN $JAVA_HOME/bin/java -version
