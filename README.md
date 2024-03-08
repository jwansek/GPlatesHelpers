# GPlatesHelpers
Quick scripts to make the GPlates software less annoying to use

Adds linebreaks to .rot files to help readability, and removes them again so the software doesn't complain

- [Download linebreakadder.exe](https://github.com/jwansek/GPlatesHelpers/releases/download/default/linebreakadder.exe)
- [Download linebreakremover.exe](https://github.com/jwansek/GPlatesHelpers/releases/download/default/linebreakremover.exe)

## Line Break Remover

`linebreakadder.exe [input .rot file] [output .rot file]` or `linebreakadder.py [input .rot file] [output .rot file]` is faster but you need python installed.

Adds linebreaks when the first number is different, e.g.:

```
[...]
100 950.0   60.4016  168.15  -17.7634  000 !
100 1000.0   90.0    0.0    0.0  000 ! Craton A Start

200  0.0   90.0    0.0    0.0  000 ! Craton B End
200  1.0   37.4047  137.7895  -78.749  000 ! Drift Correction
200 650.0   37.4047  137.7895  -78.749  000 !
200 700.0   51.9342  153.8847  -71.8022  000 !
200 750.0   62.2189  169.5583  -69.5091  000 !
200 800.0   63.134  170.375  -61.5644  000 ! Craton B (Start moving independantly)
200 800.0   90.0    0.0    0.0  100 ! Craton B (End Fol-A)
200 1000.0   90.0    0.0    0.0  100 ! Craton B Start (fol-A)

201  0.0   90.0    0.0    0.0  000 ! Ocean B1 End
201  1.0   81.6214 -144.687  -71.4834  000 ! Drift Correction
[...]
```

## Line Break Adder

`linebreakremover.exe [input .rot file] [output .rot file]` or `linebreakremover.py [input .rot file] [output .rot file]` is faster but you need python installed.

Removes all two or more linebreaks so the GPlates software doesn't complain.