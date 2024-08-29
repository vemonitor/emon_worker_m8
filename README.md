# emon_worker_m8

[![PyPI package](https://img.shields.io/pypi/v/vemonitor_m8.svg)](https://pypi.org/project/emon_worker_m8/)
[![Downloads](https://static.pepy.tech/badge/emon_worker_m8)](https://pepy.tech/project/emon_worker_m8)

> **Note**
> This repository is under active development and is not yet fully tested.

> **Warning**  
> Use this package at your own risk. Misconfiguration or bugs in this application can lead to an excessive number of disk read/writes and/or requests to designated servers (e.g., the EmonCms Server). It is essential that you fully understand and manage:
> - Your VeMonitor configuration file settings.
> - Your Redis server settings.
>
> It is strongly recommended to test your configuration using a monitoring tool like Telegraf/Grafana and Redis/Grafana to supervise and control disk read/writes and HTTP requests, ensuring they follow expected patterns.


This package is an extension of the [vemonitor_m8](https://github.com/vemonitor/vemonitor_m8) package.

It acts as an Output Worker API, tasked with sending data to an EmonCms web application.

## Configuration

To effectively manage data output and server connections, you'll need to configure both App Blocks and App Connectors in your setup.

### AppConnector Configuration

> **Warning**  
> This configuration file contains sensitive data such as API keys.  
> Ensure that file read and write permissions are properly restricted according to your editing and execution needs.

From [the App Connectors configuration file](https://github.com/vemonitor/emon_worker_m8/tree/main/config_sample/vm_appConnectors.yaml), you can define the available servers running EmonCms instances as follows:

```yaml
    appConnectors:
        # ---------------------------
        # EmonCms Server Configurations
        # ---------------------------
        emoncms:
            # key: define your desired source name
            local:
                # addr: the HTTP address of the running EmonCms instance
                addr: "http://127.0.0.1:8080"
                # Must be replaced with your Read/Write API Key
                apikey: "MY_EMONCMS_API_KEY"
```

### AppBlocks Configuration

From [the main vemonitor_m8 configuration file](https://github.com/vemonitor/emon_worker_m8/tree/main/config_sample/vm_conf.yaml), you can define an AppBlock output as follows:

```yaml
        # inputs:  
            # (...)
        outputs:
            # Define the EmonCms output type
            # Contains a list of output sending groups
            emoncms:
                -   # Name of the first output sending group
                    name: "bat_t1"
                    # App connector source
                    # Multiple EmonCms servers can be configured
                    # in the AppConnectors configuration file
                    source: "local"
                    # Object of Nodes and related input block names
                    # Each item must be formatted as:
                    # NODE_NAME: [LIST_OF_BLOCKS_NAMES]
                    # Each Block Name must correspond to an input block name.
                    columns:
                        # E
                        bmv700: [
                            'V', 'I', 'P', 'CE', 'SOC', 'Alarm',
                            'AR', 'Relay', 'H2', 'H17', 'H18'
                        ]
                    # Data time interval to compile
                    time_interval: 1
                    # Cache interval for items to send as a bulk
                    # Data length sent is time_interval * cache_interval
                    cache_interval: 10
```

## Running the Application

To execute the `BatteryMonitor` app block, use the following command: 

```
python vemonitor_m8 --block BatteryMonitor
```

This command will start the `vemonitor` `BatteryMonitor` app block instance.

To set debugging information enabled, allowing you to monitor its operation and troubleshoot any issues, use the following command:  

```
python vemonitor_m8 --block BatteryMonitor --debug
```