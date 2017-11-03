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

create(dsName, 'JDBCSystemResource')
cd('/JDBCSystemResource/' + dsName)
set('Target','AdminServer')
 
cd('/JDBCSystemResource/' + dsName +'/JdbcResource/' + dsName)

# Create JDBCDataSourceParams
cmo.setName(dsName)
cd('/JDBCSystemResource/' + dsName +'/JdbcResource/' + dsName)
create('myJdbcDataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String(dsJNDIName))
set('GlobalTransactionsProtocol', java.lang.String('None'))
 
# Create JDBCDriverParams
cd('/JDBCSystemResource/' + dsName +'/JdbcResource/' + dsName)
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName',dsDriverName)
set('URL',dsURL)
set('PasswordEncrypted', dsPassword)
set('UseXADataSourceInterface', 'false')
 
# Create JDBCDriverParams Properties'
create('myProperties','Properties')
cd('Properties/NO_NAME_0')
create('user','Property')
cd('Property')
cd('user')
set('Value', 'openshiftUser')

 
# Create JDBCConnectionPoolParams
cd('/JDBCSystemResource/' + dsName +'/JdbcResource/' + dsName)
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
set('TestTableName','SQL SELECT 1')

updateDomain()
closeDomain()
exit()
