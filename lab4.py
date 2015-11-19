#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

prov_tax = .05
fed_tax = .025


def purchase_amount(purchase):
    return "Amount of purchase: {0:.2f}".format(purchase)


def provincial_tax(purchase):
    return "Provincial tax: {0:.2f}".format(purchase * prov_tax)


def federal_tax(purchase):
    return "Federal tax: {0:.2f}".format(purchase * fed_tax)


def total_tax(purchase):
    return "Total tax: {0:.2f}".format((purchase * (prov_tax + fed_tax)))


def total_sale(purchase):
    return "Total sale: {0:.2f}".format(purchase * (1 + prov_tax + fed_tax))


def bill_of_sale(purchase):
    file_name = "bill of sale.txt"

    output_file = open(file_name, 'w')
    output_file.write(purchase_amount(purchase) + "\n")
    output_file.write(provincial_tax(purchase) + "\n")
    output_file.write(federal_tax(purchase) + "\n")
    output_file.write(total_tax(purchase) + "\n")
    output_file.write(total_sale(purchase) + "\n")


bill_of_sale(100)