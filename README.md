<!--
SPDX-License-Identifier: BSD-3-Clause
-->

# Graffle2Svg _Reloaded_

This project is a fork of [`graffle2svg`@google-code](
http://code.google.com/p/graffle2svg/).
_BUT_ the whole architecture of the program was changed,
and a lot of new features were added:

* New shapes: Diamond, Cloud
* Management of colors and sizes of arrows
* Bounding box filtering
* Speed up in processing the graffle file
* Unicode support
* Enhanced Text management

All these features were not back-ported,
due to the change of architecture.

## Installation

from source:

```shell
sudo python setup.py install
```
