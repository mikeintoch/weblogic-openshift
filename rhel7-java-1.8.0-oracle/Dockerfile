FROM registry.access.redhat.com/rhel7:latest
MAINTAINER Jose David Gamboa <jgamboag@redhat.com>

ENV JAVA_HOME="/usr/java/${JAVA_VERSION}"

# Copy binaries
# -------------
ADD ${JAVA_BASEURL}${JAVA_NAME} /tmp/

# Add Binaries and Install JDK
RUN chmod a+xr /tmp/ && \
    rpm -Uvh /tmp/${JAVA_NAME}
