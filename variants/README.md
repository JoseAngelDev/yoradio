# Variants

Each folder is one firmware variant:

```
variants/<name>/myoptions.h   # pins, display (DSP_MODEL), DAC/VS1053... (required)
variants/<name>/variant.env   # CHIP=esp32|esp32s3, PARTITION=<scheme> (optional)
```

Run **Actions → Build firmware & web flasher → Run workflow** and type `<name>` as `variant`.
`<name>` may only contain letters, digits, `.`, `_`, `-`.
