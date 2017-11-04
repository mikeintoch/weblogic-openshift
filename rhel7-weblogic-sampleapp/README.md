Example of Image with WLS Domain in OpenShift
=============================================
This Dockerfile is an OpenShift adaptation of the sample Oracle WebLogic
domain distributed by Oracle. It extends rhel7-weblogic-domain.

The upstream reference can be found here:
https://github.com/oracle/docker-images/tree/master/OracleWebLogic/samples/1221-appdeploy

Once deployed, the sample application will be available on port 8001 of
the pod.

Deploying this Application within OpenShift
===========================================

This application can be deployed using `oc new-app` pointing to the git
repository. Alternately you can build it using the following YAML:

    kind: List
    apiVersion: v1
    items:

    - kind: ImageStream
      apiVersion: v1
      metadata:
        labels:
          app: rhel7-weblogic-atmmovilapp
        name: rhel7-weblogic-atmmovilapp
      spec: {}

    - kind: BuildConfig
      apiVersion: v1
      metadata:
        labels:
          app: rhel7-weblogic-atmmovilapp
        name: rhel7-weblogic-atmmovilapp
      spec:
        output:
          to:
            kind: ImageStreamTag
            name: rhel7-weblogic-atmmovilapp:latest
        source:
          git:
            uri: https://github.com/idavistro/openshift-weblogic.git
          contextDir: rhel7-weblogic-sampleapp
          type: Git
        strategy:
          dockerStrategy:
            env:
            -name: appname
            value: atm_movil-webclient
            -name: apppkg
            value: atm_movil-webclient-1.0-SNAPSHOT.war
            -name: dsName
            value: ds_atm_movil
            -name: dsDatabaseName
            value: test
            -name: datasourceTarget
            value: AdminServer
            -name: dsJNDIName
            value: jdbc/atm_movil
            -name: dsDriverName
            value: com.mysql.jdbc.Driver
            -name: dsURL
            value: jdbc:mysql://192.168.42.1:3306/test
            -name: dsUserName
            value: openshiftUser
            -name: dsPassword
            value: R3dh4t1!
            -name: dsTestQuery
            value: SQL SELECT 1
            from:
              kind: ImageStreamTag
              name: rhel7-weblogic-domain:latest
          type: Docker
        triggers:
        - type: ConfigChange
        - imageChange: {}
          type: ImageChange

    - kind: DeploymentConfig
      apiVersion: v1
      metadata:
        labels:
          app: rhel7-weblogic-atmmovilapp
        name: rhel7-weblogic-atmmovilapp
      spec:
        replicas: 1
        selector:
          app: rhel7-weblogic-atmmovilapp
          deploymentconfig: rhel7-weblogic-atmmovilapp
        strategy:
          resources: {}
        template:
          metadata:
            annotations:
              openshift.io/container.rhel7-weblogic-atmmovilapp.image.entrypoint: '["startWebLogic.sh"]'
            labels:
              app: rhel7-weblogic-atmmovilapp
              deploymentconfig: rhel7-weblogic-atmmovilapp
          spec:
            containers:
            - image: rhel7-weblogic-atmmovilapp:latest
              name: rhel7-weblogic-atmmovilapp
              ports:
              - containerPort: 8001
                protocol: TCP
        triggers:
        - type: ConfigChange
        - imageChangeParams:
            automatic: true
            containerNames:
            - rhel7-weblogic-atmmovilapp
            from:
              kind: ImageStreamTag
              name: rhel7-weblogic-atmmovilapp:latest
          type: ImageChange

    - kind: Service
      apiVersion: v1
      metadata:
        labels:
          app: rhel7-weblogic-atmmovilapp
        name: rhel7-weblogic-atmmovilapp
      spec:
        ports:
        - name: 8001-tcp
          port: 8001
          protocol: TCP
          targetPort: 8001
        selector:
          app: rhel7-weblogic-atmmovilapp
          deploymentconfig: rhel7-weblogic-atmmovilapp
