<!--
SPDX-FileCopyrightText: 2012 Jean-Noel Avila <jn.avila@free.fr>
SPDX-FileCopyrightText: 2022 Jean-Noël Avila <jn.avila@free.fr>
SPDX-FileCopyrightText: 2023 Robin Vobruba <hoijui.quaero@gmail.com>

SPDX-License-Identifier: BSD-3-Clause
-->

# Graffle2Svg _Reloaded_

[![License: BSD-3-Clause](
    https://img.shields.io/badge/License-BSD--3--Clause-blue.svg)](
    https://spdx.org/licenses/BSD-3-Clause.html)
[![REUSE status](
    https://api.reuse.software/badge/github.com/hoijui/graffle2svg)](
    https://api.reuse.software/info/github.com/hoijui/graffle2svg)

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
