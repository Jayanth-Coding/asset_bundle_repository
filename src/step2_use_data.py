# Databricks notebook source
total = dbutils.jobs.taskValues.get(taskKey="make_data", key="total", debugValue=0)
print(f"Step 2: received {total}, doubled it is {total * 2}")