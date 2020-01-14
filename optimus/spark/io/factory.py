from optimus.helpers.raiseit import RaiseIt
from optimus.spark.io.drivers.abstract_driver import AbstractDriver
from optimus.spark.io.drivers.cassandra import CassandraDriver
from optimus.spark.io.drivers.mysql import MySQLDriver
from optimus.spark.io.drivers.oracle import OracleDriver
from optimus.spark.io.drivers.postgresql import PostgreSQLDriver
from optimus.spark.io.drivers.presto import PrestoDriver
from optimus.spark.io.properties import DriverProperties
from optimus.spark.io.drivers.redshift import RedshiftDriver
from optimus.spark.io.drivers.sqlite import SQLiteDriver
from optimus.spark.io.drivers.sqlserver import SQLServerDriver


class DriverFactory:
    """Database driver factory. This database driver factory currently supports the following implementations:

        * Cassandra
        * MySQL
        * Oracle
        * Postgres
        * Presto
        * Redshift
        * SQLite
        * SQLServer
    """

    @staticmethod
    def get(driver_type) -> AbstractDriver:
        """
        Returns a driver implementation given a database name

        :param driver_type: name of the database
        :return: a database driver
        """
        if driver_type == DriverProperties.CASSANDRA.value["name"]:
            return CassandraDriver()
        elif driver_type == DriverProperties.MYSQL.value["name"]:
            return MySQLDriver()
        elif driver_type == DriverProperties.ORACLE.value["name"]:
            return OracleDriver()
        elif driver_type == DriverProperties.POSTGRESQL.value["name"]:
            return PostgreSQLDriver()
        elif driver_type == DriverProperties.PRESTO.value["name"]:
            return PrestoDriver()
        elif driver_type == DriverProperties.REDSHIFT.value["name"]:
            return RedshiftDriver()
        elif driver_type == DriverProperties.SQLITE.value["name"]:
            return SQLiteDriver()
        elif driver_type == DriverProperties.SQLSERVER.value["name"]:
            return SQLServerDriver()
        else:
            RaiseIt.value_error(driver_type, [database["name"] for database in DriverProperties.list()])
