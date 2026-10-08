# Databricks notebook source
print("Hello from my first bundle!")

# Databricks notebook source
dbutils.widgets.text("greeting", "no greeting given")
greeting = dbutils.widgets.get("greeting")
print(f"Message: {greeting}")