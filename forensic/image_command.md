# Image command helper

Create image

```bash
    dd if=/dev/cdrom of=image.dd
```

Convert raw image to vmdk

```bash
    qemu-img convert -O vmdk imagefile.dd vmdkname.vmdk
```

```bash
    VBoxManage convertfromraw imagefile.dd vmdkname.vmdk --format VMDK
```