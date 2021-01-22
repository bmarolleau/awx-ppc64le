How to build AWX on ppc64le and non-x86 Architecture?
---

Fork for ppc64le, below, the original links and instructions.
- For OpenShift deployment: `oc login` , `podman login` then execute the following playbook:

`ansible-playbook -vvv -i inventory install.yml -e openshift_password=redhat  -e docker_registry_password=$(oc whoami -t) -e tini_architecture=ppc64le -e kubectl_architecture=ppc64le `

Known Issues and Workarounds 
---
- BUG  update forever after start documented [here](https://github.com/ansible/awx/issues/3032)
On the AWX Pod: 

`awx-manage migrate --noinput`

`awx-manage provision_instance --hostname=$(hostname)`

`awx-manage register_queue --queuename=tower --instance_percent=100`

- Pb with user admin (not created, pb with Ansible playbook ? to investigate)
Documented [here](https://docs.ansible.com/ansible-tower/3.2.5/html/administration/tipsandtricks.html#index-3)
On the AWX Pod, create the admin user:

`awx-manage createsuperuser`

Initial AWX Documentation
---

AWX provides a web-based user interface, REST API, and task engine built on top of [Ansible](https://github.com/ansible/ansible). It is the upstream project for [Tower](https://www.ansible.com/tower), a commercial derivative of AWX.  

To install AWX, please view the [Install guide](./INSTALL.md).

To learn more about using AWX, and Tower, view the [Tower docs site](http://docs.ansible.com/ansible-tower/index.html).

The AWX Project Frequently Asked Questions can be found [here](https://www.ansible.com/awx-project-faq).

The AWX logos and branding assets are covered by [our trademark guidelines](https://github.com/ansible/awx-logos/blob/master/TRADEMARKS.md).

