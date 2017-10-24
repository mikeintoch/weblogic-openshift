FROM registry.access.redhat.com/rhel7:latest
MAINTAINER Johnathan Kupferer <jkupfere@redhat.com>

ENV JAVA_VERSION=${JAVA_VERSION:-1.8.0} \
    JAVA_TYPE=${JAVA_TYPE:-oracle}

ENV JAVA_HOME=/usr/lib/jvm/java-${JAVA_VERSION}-${JAVA_TYPE}

RUN yum repolist --disablerepo=* && \
    yum-config-manager --disable \* > /dev/null && \
    yum-config-manager --enable rhel-7-server-rpms > /dev/null \
    yum-config-manager --enable rhel-7-server-extras-rpms > /dev/null \
    yum-config-manager --enable rhel-7-server-optional-rpms > /dev/null \
    yum-config-manager --enable rhel-7-server-thirdparty-oracle-java-rpms > /dev/null \
      install -y \
      java-${JAVA_VERSION}-${JAVA_TYPE}-devel \
      java-${JAVA_VERSION}-${JAVA_TYPE}-jdbc && \
    yum clean all
