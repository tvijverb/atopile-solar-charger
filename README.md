# atopile-solar-charger

## Description
### WARNING: PCB is still untested, it's being produced right now. I'll update the readme after testing.
Solar charger PCB using the Texas Instruments BQ25504. It is meant to be paired with a LIC supercap https://www.aliexpress.com/w/wholesale-lic-supercapacitor.html?spm=a2g0o.home.search.0
Pairing it with a regular 3.7V litihium battery is not recommended since the undervoltage value is too low for this chemistry.

Solar input - 3V max

Battery voltage range

| Specs | Voltage |
| --- | --- |
| Vbat_ov | 3.8 |
| Vbat_uv | 2.5 |
| Vbat_ok | 2.6 |

# Design files
The JLCPCB production files can be found in the following folder
```
elec/layout/default/production
```

## Connectors
There are 3 2-pin JST connectors with a 2mm pitch. Positive and negative pins are indicated with a + sign on the top of the PCB.
1. Solar input
2. battery connector
3. load output

## Silkscreen
The component silkscreen labels have not been modified (yet) from default settings. These will cause warnings in KiCad DRC checks.

## Atopile CI/CD
The atopile CI/CD github action pipeline will currently give errors since I used my own parts-search endpoint. This will probably be fixed in the coming weeks.
