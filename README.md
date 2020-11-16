# docker-python-hbase
Provides an image with Python to access a HBase Cluster with Kerberos and Thrift.

## Description

This image based on centos:7 provides dependencies when running Python applications connecting to HBase using Thrift and Kerberos.

## Example
Example using the docker [image](https://hub.docker.com/r/leandropsilva/hbase-python).
```
docker pull leandropsilva/hbase-python
docker run \
    --volume ${PWD}/src:/src/ \
    -it \
    --name hbase-python01 \
    --rm leandropsilva/hbase-python
```

