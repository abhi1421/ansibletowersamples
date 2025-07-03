# Package Management Role

This role manages software packages using `yum` and `rpm` in air-gapped RHEL environments. It supports multiple operations with a single action keyword.

## 🔧 Extra Vars (via AAP)

| Variable       | Required | Description                                  |
|----------------|----------|----------------------------------------------|
| `pkg_action`   | Yes      | install, remove, update, info, list_installed, list_available |
| `pkg_name`     | Conditional | Name of the package(s) (not needed for list actions) |

## ✅ Supported Actions

- `install`: Install specified package(s)
- `remove`: Remove specified package(s)
- `update`: Update specified package(s)
- `info`: Get package details via `rpm -qi`
- `list_installed`: List all installed packages
- `list_available`: List all available packages from repo

## ⚠️ Notes

- Only built-in Ansible modules used (`yum`, `command`, `rpm`).
- Works in air-gapped systems with local or Satellite-connected repos.