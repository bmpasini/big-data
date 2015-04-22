#!/usr/bin/python
import sys
import os

revenue_list = {}

def inv_revenue_list(revenue_list):
    inv_revenue_list = []
    for key, value in revenue_list.items():
        inv_revenue_list.append((value, key))
    return sorted(inv_revenue_list, reverse = True)

for line in sys.stdin:
    
    agent_name, revenue = line.strip().split("&", 1)
    
    try:
        revenue = float(revenue)
    except ValueError:
        continue
    
    if agent_name not in revenue_list:
        revenue_list[agent_name] = revenue
    else:
        revenue_list[agent_name] += revenue

inv_revenue_list = inv_revenue_list(revenue_list)

for agent_name in inv_revenue_list[:10]:
    print ("KEY: %s        VALUE: %d" % (agent_name[1], agent_name[0]))