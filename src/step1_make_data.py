# Databricks notebook source
numbers = [10, 20, 30, 40]
total = sum(numbers)
print(f"Step 1: total is {total}")

dbutils.jobs.taskValues.set(key="total", value=total)