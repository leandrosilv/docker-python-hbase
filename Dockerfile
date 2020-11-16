FROM centos:7

RUN yum -y update \
  && yum -y install epel-release \
  && yum -y install python-devel \
  && yum -y install gcc-c++ \
  && yum -y install python-thrift \
  && yum -y install openldap-devel \
  && yum -y install python-six \
  && yum -y install python-backports \
  && yum -y install libquadmath \
  && yum -y install libgfortran \
  && yum -y install python-pip \
  && yum -y install gcc \
  && yum -y install krb5-devel \
  && yum -y install krb5-workstation \
  && yum clean all \
  && rm -rf /var/cache/yum/*

RUN pip2 install thrift==0.9.3 \
  && pip2 install thrift-sasl==0.3.0 \
  && pip2 install thriftpy==0.3.9 \
  && pip2 install six==1.12.0 \
  && pip2 install pure-sasl==0.5.0 \
  && pip2 install setuptools==3.4.4 \
  && pip2 install impyla==0.13.8 \
  && pip2 install pykerberos==1.1.14 \
  && pip2 install PyGSSAPI==1.0.0 \
  && pip2 install gssapi==1.5.1 \
  && pip2 install tendo==0.2.15 \
  && rm -rf ~/.cache/pip/

COPY ./app/hbase/ /app/hbase