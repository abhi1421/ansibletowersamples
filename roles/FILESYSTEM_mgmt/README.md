# Filesystem Management Role

This role performs unified filesystem and LVM management using a single action keyword. It supports operations such as LVM creation, formatting, mounting, resizing, and removal.

## 🔧 Extra Vars (via AAP)

| Variable     | Required  | Description                                 |
|--------------|-----------|---------------------------------------------|
| fs_action    | Yes       | One of: create_lvm, format_fs, mount_fs, unmount_fs, resize_fs, remove_lv |
| fs_disk      | Cond      | Disk device (e.g., /dev/sdb), needed for LVM |
| fs_vg        | Cond      | Volume group name                           |
| fs_lv        | Cond      | Logical volume name                         |
| fs_size      | Cond      | Size for LV (e.g., 5G)                      |
| fs_path      | Cond      | Mount point path (e.g., /data)             |
| fs_fstype    | Optional  | Filesystem type (default: xfs)             |

## ✅ Supported Actions

- `create_lvm`: Create PV, VG, and LV
- `format_fs`: Format LV as a filesystem
- `mount_fs`: Mount the LV to a path
- `unmount_fs`: Unmount a mounted path
- `resize_fs`: Resize XFS filesystem
- `remove_lv`: Remove logical volume

## 🛑 Warning

Ensure backups before resizing or removing volumes.