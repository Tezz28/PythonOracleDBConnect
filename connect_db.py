import cx_Oracle
import sys
import os
import yaml


def connectOracle():
    # Get DB configurations from db_config.yaml
    with open("db_config.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        print("Config Read successful")

    host = data[0]['DB']['HOST']
    port = data[0]['DB']['PORT']
    service_name = data[0]['DB']['SERVICE_NAME']
    user = data[0]['DB']['USER']
    password = data[0]['DB']['PASSWORD']

    try:
        if sys.platform.startswith("darwin"):
            lib_dir = os.path.join(os.environ.get("HOME"), "Downloads",
                                   "instantclient_21_3")
            cx_Oracle.init_oracle_client(lib_dir=lib_dir)
        elif sys.platform.startswith("win32"):
            lib_dir = r"C:\Oracle\instantclient-basic-windows.x64-21.3.0.0.0\instantclient_21_3"
            cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    except Exception as err:
        print("Whoops!")
        print(err);
        sys.exit(1);

    dsn_tns = cx_Oracle.makedsn(host, port,
                                service_name=service_name)
    conn = cx_Oracle.connect(user=user, password=password,
                             dsn=dsn_tns)
    print('connected...')
    return conn
