# Systemd Open Files
> #systemd #limit

## Query open files for a service

Open files for a process or systemd service.

1. Query for PID and any children PID's of target service.
2. Identify child PIDS

    ```bash
    # For the actual number of open files, all PIDs will need to be checked recursively for any additional child processes.
    # Use the below in a structured loop to gather all PID's. 
    pgrep -P $pid
    ```

Any open files in `/proc/${pid}/fd/` should be counted (except for 0, 1 and 2).

## Query open file limits

### Service

```bash
systemctl show ${service_name} -p LimitNOFILE
```

### User

Open a shell as the user to see the defined limits. 

```bash
ulimit -a
```

### Filesystem

The max number of file descriptors that the Linux kernel will allow to be opened system-wide. 
```console 
# cat /proc/sys/fs/file-max
79103266
```

The `file-nr` provides three values: number of allocated file descriptors, number of free file descriptors, and max number of file descriptors
```console
# cat /proc/sys/fs/file-nr
9216	0	79103266
```

## Defining open file limits

Limits should be defined differently depending on scope. Depending on the purpose, often either approach can be taken. 

1. Using a drop-in systemd configuration modifies or extends service unit configurations.
2. Using limits.d sets resource limits for users or groups.

### Drop-in Systemd configuration

Create a drop-in configuration in the service's configuration directory for systemd. If the directory does not exist, create one. 

```console
# cat >/etc/systemd/system/${service_name}.service.d/filelimit.conf <<EOF
[Service]
LimitNOFILE=500000
EOF
```

Reload the systemd daemon to apply changes.

```bash
systemctl daemon-reload
```

Restart the service.

```bash
systemctl restart ${service_name}
```

#### Define file limits for all services

The `/etc/systemd/system.conf` file (or `/etc/systemd/system.conf.d/` directory in some cases) is used to set system-wide configuration options that affect the behavior of systemd and its services. Anything defined within this file can be overridden by service-specific configuration files or drop-in files.

Common settings include:
* `DefaultTaskMax`: Defines the maximum number of tasks (processes or threads) that can be created by a service.
* `DefaultTimeoutStartSec`: Sets the default timeout for starting services. If a service does not start within this time, it will be considered failed.
* `DefaultTimeoutStopSec`: Sets the default timeout for stopping services.
* `DefaultLimitNOFILE`: Specifies the default limit on the number of open file descriptors for services.
* `DefaultLimitNPROC`: Sets the default limit on the number of processes that can be created by services.

```console
# cat /etc/systemd/system.conf
[Manager]
DefaultStartLimitInterval=1s
DefaultStartLimitBurst=65535
DefaultTasksMax=65535
```

### Using limitsd

This requires creating a configuration file in `/etc/security/limits.d/` for the target service.

You can define hard and soft limits using `limits.d`. The example below shows the system default limits. This file will be processed first. 

```console
# cat /etc/security/limits.d/limits.conf
*       -       stack   unlimited
*       hard    nofile  4096
*       -       memlock unlimited
```


While there are no requirements for filenames, it's common practice to prefix additional files with a numbering system to control the order in which files are processed. 

For example:
- `10-user-limits.conf`: User-specific limits
- `20-group-limits.conf`: Group-specific limits
- `30-service-limits.conf`: Service-specific limits

> [!NOTE]
> Best practices:
> * Use a consistent numbering scheme to ensure that files are processed in the desired order.
> * Keep filenames descriptive to clarify their purpose.
> * Avoid using special characters or spaces in filenames to prevent issues during processing.

If you notice the example above, using `limits.d` allows you to cast sort of a wider net, whereas the systemd limits are focused on Service.

```bash
# Example: Creating limits.d file for Icinga2
# cat /etc/security/limits.d/10-icinga.conf
icinga soft nofile 65535
icinga hard nofile 65535
```

## Related

The `/etc/systemd/system.conf` file is used to set system-wide configuration options that affect the behavior of systemd and its services. Anything defined within this file can be overridden by service-specific configuration files or drop-in files.

Common settings include:
* `DefaultTaskMax`: Defines the maximum number of tasks (processes or threads) that can be created by a service.
* `DefaultTimeoutStartSec`: Sets the default timeout for starting services. If a service does not start within this time, it will be considered failed.
* `DefaultTimeoutStopSec`: Sets the default timeout for stopping services.
* `DefaultLimitNOFILE`: Specifies the default limit on the number of open file descriptors for services.
* `DefaultLimitNPROC`: Sets the default limit on the number of processes that can be created by services.




## Additional resources
- [Icinga2/Nagios monitoring plugin](https://exchange.icinga.com/winem/check_systemd_service_open_files)

