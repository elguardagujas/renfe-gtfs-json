#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base_scripts.tools import update

update.process({
  "renfeld":   "https://nap.transportes.gob.es/api/v2/fichero/1098/descarga",
  "cercanias": "https://nap.transportes.gob.es/api/v2/fichero/1130/descarga",
}, dumper="gtfs_json_dump.py")

