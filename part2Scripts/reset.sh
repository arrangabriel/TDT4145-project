#!/usr/bin/env bash

rm coffeeDB.db
python createTables.py
python fillExampleData.py