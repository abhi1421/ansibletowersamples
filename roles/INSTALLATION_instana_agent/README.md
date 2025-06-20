Ansible Role: INSTALLATION_Instana_Agent
This role automates the installation and management of the Instana agent on target nodes.

Requirements
Ansible 2.9 or higher.

Target nodes must be running a supported RPM-based Linux distribution (e.g., RHEL, CentOS, Fedora) or AIX.

Python and libselinux-python (if SELinux is enforced) on target nodes.

Privileges (sudo) to install packages, modify /etc/hosts, and manage system services.

Role Variables
instana_rpm_base_name (default: "instana-agent-static-j9-20250618-0909"): The base filename of the Instana RPMs. The role appends .<architecture>.rpm.

instana_service_name (default: "instana-agent"): The name of the Instana agent systemd service.

instana_target_dir (default: "/home/ansible"): The directory on the target node where RPMs will be copied.

instana_env_vars_script (default: "/etc/profile.d/instana.sh"): The path to the script where Instana environment variables will be set.

Files
Ensure the following files are present in the files/ directory of this role:

instana-agent-static-j9-20250618-0909.aix.rpm: Instana agent RPM for AIX.

instana-agent-static-j9-20250618-0909.s390x.rpm: Instana agent RPM for s390x.

instana-agent-static-j9-20250618-0909.x86_64.rpm: Instana agent RPM for x86_64.

instana_host_entries.txt: A plain text file with one host entry per line (e.g., 192.168.1.100 myhost.instana.com).

instana_env_vars.txt: A plain text file with one environment variable export per line (e.g., export INSTANA_AGENT_KEY="your_key").

Usage
To use this role, execute the playbook like install_instana.yml:

---
- name: Install and Configure Instana Agent
  hosts: your_target_group
  become: true # Use sudo for privileged operations
  roles:
    - INSTALLATION_Instana_Agent

Then run the playbook:

ansible-playbook -i your_inventory_file install_instana.yml

Idempotency for Host Entries
The role uses the ansible.builtin.lineinfile module with state: present to manage /etc/hosts and the environment variable script. This module is inherently idempotent:

If a line from instana_host_entries.txt or instana_env_vars.txt already exists exactly in the target file (/etc/hosts or instana.sh), Ansible will detect no change and will not re-add it.

If a new entry is added to instana_host_entries.txt or instana_env_vars.txt and then the role is re-executed, only the new line(s) will be added to the target file.