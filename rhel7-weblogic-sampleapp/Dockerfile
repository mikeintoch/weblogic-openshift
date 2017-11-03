# LICENSE CDDL 1.0 + GPL 2.0
#
# Adapted from ORACLE DOCKERFILES PROJECT
# --------------------------
# This Dockerfile extends the Oracle WebLogic image built as rhel7-weblogic-domain.
#
# It will deploy any package defined in APP_PKG_FILE located in APP_PKG_LOCATION
# into the DOMAIN_HOME with name defined in APP_NAME
#
#
# ENVIRONMENT VARIABLES
# ---------------------
#
# APP_NAME - Application name for deployment.
#
# APP_PKG_FILE - Name of war file  te deploy
#
# APP_PKG_LOCATION - default: /u01/oracle
#
#
FROM rhel7-weblogic-domain
MAINTAINER Johnathan Kupferer <jkupfere@redhat.com>

# Define variables with default values
#ENV APP_NAME=${APP_NAME:-sample} \
 #   APP_PKG_FILE=${APP_PKG_FILE:-sample.war} \
  #  APP_PKG_LOCATION=${APP_PKG_LOCATION:-/u01/oracle}

ENV APP_NAME=atm_movil-webclient \
    APP_PKG_FILE=atm_movil-webclient-1.0-SNAPSHOT.war \
    APP_PKG_LOCATION=${APP_PKG_LOCATION:-/u01/oracle}

# WLS Configuration (editable during runtime)
# ---------------------------
ENV ADMIN_HOST="wlsadmin" \
    NM_PORT="5556" \
    MS_PORT="7001" \
    DEBUG_PORT="8453" \
    CONFIG_JVM_ARGS="-Dweblogic.security.SSL.ignoreHostnameVerification=true"

# WLS Configuration (persisted. do not change during runtime)
# -----------------------------------------------------------
ENV DOMAIN_NAME="${DOMAIN_NAME:-base_domain}" \
    DOMAIN_HOME=/u01/oracle/user_projects/domains/${DOMAIN_NAME:-base_domain} \
    ADMIN_PORT="${ADMIN_PORT:-8001}" \
    CLUSTER_NAME="${CLUSTER_NAME:-DockerCluster}" \
    debugFlag="${DEBUG_FLAG:-false}" \
    PRODUCTION_MODE="${PRODUCTION_MODE:-prod}" \
    PATH=$PATH:/u01/oracle/oracle_common/common/bin:/u01/oracle/wlserver/common/bin:/u01/oracle/user_projects/domains/${DOMAIN_NAME:-base_domain}/bin:/u01/oracle

# Copy files and deploy application in WLST Offline mode
ADD http://192.168.42.1/atm_movil-webclient-1.0-SNAPSHOT.war /u01/oracle/
COPY container-scripts/* /u01/oracle/

RUN chmod +xr $APP_PKG_FILE && \
    wlst /u01/oracle/app-datasource.py && \
    # wlst /u01/oracle/app-deploy.py && \
    find /u01 -user oracle -exec chmod a+rwX /u01 {} ';'
