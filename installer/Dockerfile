
# Latest version of centos
FROM centos:centos7
MAINTAINER bmarolleau
RUN yum clean all && \
    yum -y install epel-release && \
    yum -y install PyYAML python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools git python-pip && \
RUN mkdir /etc/ansible/
RUN echo -e '[local]\nlocalhost' > /etc/ansible/hosts
RUN pip install ansible
RUN yum -y install --disablerepo='*' --enablerepo='copr:copr.fedorainfracloud.org:mrmeee:ansible-awx, rhel-7-for-power-le-rpms, rhel-7-for-power-le-optional-rpms' -x *-debuginfo,*-sphinx-*,rh-python36-python-test rh-python36*
RUN yum install -y ansible-awx
