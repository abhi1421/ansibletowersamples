# Firewall Management Role

This role manages firewalld on RHEL systems in air-gapped environments, supporting services, ports, and zone operations via a single action keyword.

## 🔧 Extra Vars (via AAP)

| Variable         | Required | Description                                    |
|------------------|----------|------------------------------------------------|
| `fw_action`      | Yes      | One of: add, remove, block_port, unblock_port, enable, disable, reload, status |
| `fw_service`     | No       | Firewall service name (e.g., ssh, http)       |
| `fw_port`        | No       | Port or port/proto (e.g., 8080/tcp)           |
| `fw_zone`        | No       | Firewall zone (default: public)               |
| `fw_permanent`   | No       | Whether the rule is permanent (default: true) |

## ✅ Supported Actions

- `add`: Allow a service (e.g., ssh)
- `remove`: Remove a service
- `block_port`: Open a port
- `unblock_port`: Close a port
- `enable`: Enable firewalld
- `disable`: Stop firewalld
- `reload`: Reload configuration
- `status`: Show firewall state

## 🔐 Security Note

This role assumes `firewalld` is already installed. It does not allow raw iptables manipulation for security compliance.