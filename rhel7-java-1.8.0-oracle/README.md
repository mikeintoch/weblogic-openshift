RHEL7 with Oracle java 1.8.0
============================

This Dockerfile provides a basic RHEL7 docker image with java oracle 1.8.0
packages installed.

Deploying this Application within OpenShift
===========================================

This image builder can be deployed using the following YAML:

    kind: List
    apiVersion: v1
    items:

    - kind: ImageStream
      apiVersion: v1
      metadata:
       name: rhel7
      spec:
        tags:
        - from:
            kind: DockerImage
          name: registry.access.redhat.com/rhel7:latest
      name: latest

    - kind: ImageStream
      apiVersion: v1
      metadata:
        labels:
          app: rhel7-java-180-oracle
        name: rhel7-java-180-oracle
      spec: {}  

    - kind: BuildConfig
      apiVersion: v1
      metadata:
        labels:
          app: rhel7-java-180-oracle
        name: rhel7-java-180-oracle
      spec:
        output:
          to:
            kind: ImageStreamTag
            name: rhel7-java-180-oracle:latest
      source:
        type: Git
        git:
          uri: https://github.com/idavistro/openshift-weblogic.git
        contextDir: rhel7-java-1.8.0-oracle
      strategy:
        dockerStrategy:
          env:
          - name: JAVA_BASEURL
            value: http://192.168.42.1/
          - name: JAVA_NAME
            value: jdk-8u151-linux-x64.rpm
          - name: JAVA_VERSION
            value: jdk1.8.0_151
          from:
            kind: ImageStreamTag
            name: rhel7:latest
          type: Docker
    triggers:
    - type: ConfigChange
    - type: ImageChange
      imageChange: {}
