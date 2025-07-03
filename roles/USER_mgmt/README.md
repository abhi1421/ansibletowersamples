# User Management Role (Bank-Grade, Unified)

This role provides full user lifecycle management in an air-gapped environment using AAP.

## 🔧 Input (via Extra Vars)

| Variable        | Required | Description                                         |
|----------------|----------|-----------------------------------------------------|
| `user_action`  | Yes      | Action keyword (e.g., `add`, `delete`, etc.)        |
| `username`     | Yes      | Target system username                              |
| `user_shell`   | No       | Shell (used in add/modify/enablelogin)              |
| `user_home`    | No       | Home directory (add/modify)                         |
| `user_password`| No       | Hashed password (used in add/passwd)                |
| `user_groups`  | No       | List of groups (used in group mgmt actions)         |

## ✅ Supported Actions

- `add` — Add user
- `delete` — Delete user
- `modify` — Modify shell/home
- `lock` — Lock account
- `unlock` — Unlock account
- `passwd` — Change password (hashed)
- `expire` — Expire password (forces change)
- `nologin` — Set shell to `/sbin/nologin`
- `enablelogin` — Restore shell from `user_shell`
- `status` — Print user status
- `groupset` — Overwrite group membership
- `groupadd` — Add to groups (append)
- `groupremove` — Remove from groups

## 🔐 Password Hashing Example

```bash
openssl passwd -6 'StrongPassword'