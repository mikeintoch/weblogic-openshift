import os

# Deployment Information 
domain_name  = os.environ.get("DOMAIN_NAME", "base_domain")
domainhome = os.environ.get('DOMAIN_HOME', '/u01/oracle/user_projects/domains/base_domain')
appname    = os.environ.get('APP_NAME', 'atm_movil-webclient')
apppkg     = os.environ.get('APP_PKG_FILE', 'atm_movil-webclient-1.0-SNAPSHOT.war')
appdir     = os.environ.get('APP_PKG_LOCATION', '/u01/oracle')
cluster_name = os.environ.get("CLUSTER_NAME", "DockerCluster")

# Definition DataSource Properties
dsName            = "ds_atm_movil"
dsDatabaseName    = "test"
datasourceTarget  = "AdminServer"
dsJNDIName        = "jdbc/atm_movil"
dsDriverName      = "com.mysql.jdbc.Driver"
dsURL             = "jdbc:mysql://192.168.42.1:3306/test"
dsUserName        = "openshiftUser"
dsPassword        = "R3dh4t1!"
dsTestQuery       = "SQL SELECT 1"

# Read Domain in Offline Mode
# ===========================
readDomain(domainhome)

# Create DataSource
# ==================
cd('/')
cmo.createJDBCSystemResource(dsName);
cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName)
cmo.setName(dsName)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName )
set('JNDINames',jarray.array([String(dsJNDIName)], String))
 
cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName )
cmo.setUrl(dsURL)
cmo.setDriverName( dsDriverName )
cmo.setPassword(dsPassword)
 
cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCConnectionPoolParams/' + dsName )
cmo.setTestTableName(dsTestQuery)

#cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName )
#cmo.createProperty('user')
 
#cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName + '/Properties/user')
#cmo.setValue(dsUserName)
 
#cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName )
#cmo.createProperty('databaseName')
 
#cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName + '/Properties/databaseName')
#cmo.setValue(dsDatabaseName)
 
#cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName )
#cmo.setGlobalTransactionsProtocol('OnePhaseCommit')
 
cd('/SystemResources/' + dsName )
set('Targets',jarray.array([ObjectName('com.bea:Name=' + datasourceTarget + ',Type=Server')], ObjectName))

save()
activate()

#updateDomain()
#closeDomain()
exit()
