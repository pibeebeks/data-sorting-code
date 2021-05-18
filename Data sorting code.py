#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:36:55 2019

@author: lumi
"""


#%%
import pandas as pd
import csv

kpmg_data_set = pd.ExcelFile('/Users/lumi/Downloads/KPMG_VI_New_raw_data_update_final (1).xlsx')
transactions = pd.read_excel(kpmg_data_set, 'Transactions')
new_customers = pd.read_excel(kpmg_data_set, 'NewCustomerList')
customer_demographics = pd.read_excel(kpmg_data_set, 'CustomerDemographic')
customer_addresses = pd.read_excel(kpmg_data_set, 'CustomerAddress')


#creating a function to add column items to a list
def add_to_list(sheet_name,column_name):
    list_name = []
    for item in sheet_name[column_name]:
        list_name.append(item)
    return(list_name)

#created list of cusomter ids
customer_id = add_to_list(transactions,'customer_id')



#creating function to count frequency of each element in a list and store in dic
#def count_times_in_list(list_name):  #big'o depends on length of list for both. but this is longer
#    times_in_list = {}
#    for item in list_name:
#        if item in times_in_list:
#            times_in_list[item] += 1
#        else:
#            times_in_list[item] = 1
#   
#    return times_in_list  

def count_times_in_list(list_name): #uses the count method so reduces the big'o notion
    times_in_list = {}
    for item in list_name:
        times_in_list[item] = list_name.count(item)
    return times_in_list


customer_id_frequency = count_times_in_list(customer_id)

#create function to arrange in descending order of values

def arrange_dic(dic_name):
    # create a tuple list  sorted by index[1]; value field
    listoftuples =  sorted(dic_name.items(), reverse=True, key=lambda x: x[1])
    # iterate over the sorted sequence 
    new_dic = {}
    for elem in listoftuples:
        new_dic[elem[0]] = elem[1]
    return new_dic

arranged_customer_id = arrange_dic(customer_id_frequency)
    
#create a function that takes customer_id and the gender

#def customer_to_gender(sheetname, columnname, columnname2):
#    customer_to_gender = dict(zip(sheetname[columnname],sheetname[columnname2]))
#        
#    return customer_to_gender
#        
customer_to_gender =  dict(zip(customer_demographics['customer_id'],customer_demographics['gender']))
customer_to_agegroup = dict(zip(customer_demographics['customer_id'],customer_demographics['age_group']))
customer_to_residence = dict(zip(customer_addresses['customer_id'],customer_addresses['state'])) 
# create a tuple of customer id, number of transactions, residence, agegroup and gender

def customer_info(dic1, dic2, dic3, dic4):
    lis1 = [[k,v] for k,v in dic1.items()]
    lis2 = [[k,v] for k,v in dic2.items()]
    lis3 = [[k,v] for k,v in dic3.items()]
    lis4 = [[k,v] for k,v in dic4.items()]
    
    for items in range(len(lis1)):
        for i in range(len(lis2)):
            if lis1[items][0] == lis2[i][0]:
                lis1[items].append(lis2[i][1])
            
    
    for items in range(len(lis1)):
        for i in range(len(lis3)):
            if lis1[items][0] == lis3[i][0]:
                lis1[items].append(lis3[i][1])
           
                
    for items in range(len(lis1)):
        for i in range(len(lis4)):
            if lis1[items][0] == lis4[i][0]:
                lis1[items].append(lis4[i][1]) 
            
            
    return lis1
#creating a list of lists with dic keys and values
# merging all the lists in one list
    
#exporting to csv
with open("customer_info", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(customer_info)
#writer.writerows(listname)    
    
    
#to get the number of transactions done by different age groups

#to get the number of transactions done by different gender
#to get the number of transactions done by different residences
