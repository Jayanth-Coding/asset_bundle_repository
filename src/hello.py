# Databricks notebook source
print("Hello from my Github to Databricks deployment practice!")

# Databricks notebook source
dbutils.widgets.text("greeting", "no greeting given")
greeting = dbutils.widgets.get("greeting")
print(f"Message: {greeting}")