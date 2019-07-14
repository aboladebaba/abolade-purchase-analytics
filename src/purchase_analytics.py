import csv, sys

def purchase_analytics(fileA, fileB, fileC):
    """
    Parses two input files and writes report to an output file.

    Parameters
    ----------
    fileA: string (required)
        The name of the first file (e.g. order_products.csv)
    fileB: string (required)
        The second file to parse (e.g. products.csv)
    fileC: string (required)
        The output file (e.g. report.csv)
    
    Output
    ------
    Generate report.csv file.
    """
    with open(fileA, 'r') as fha:
        raw = csv.reader(fha)
        next(raw, None)
        rawOrders = {}
        for line in raw:
            temp = rawOrders.get(line[1], [])
            temp.append(line[3])
            rawOrders[line[1]] = temp
    fha.close()

    with open(fileB, 'r') as fhb:
        raw = csv.reader(fhb)
        next(raw, None)
        rawProducts = {}
        for line in raw:
            temp = rawProducts.get(line[0], [])
            temp.append(line[3])
            rawProducts[line[0]] = temp
    fhb.close()
    # Sanity check to ensure no single product is associated with multiple departments
    # This should give an empty list 
    #prodMultipleDept = [k for k,v in deptProd.items() if len(v) > 1] # this list was empty

    # Merge the two dict objects base on common keys - product_ids
    merged = { key: (rawOrders[key], rawProducts[key]) for key in rawOrders}
    
    #Build a dict object with Department_id as key 
    aggDept = {} 
    for key, val in merged.items():
        dept = val[1][0] # pull out the department_id
        numOrdered = len(val[0]) # number of times this product was ordered by the department
        numFirst = val[0].count('0') # number of times the products was ordered for the first time
        res = numOrdered, numFirst
        temp = aggDept.get(dept, [])
        temp.append(res)
        aggDept[dept] = temp

    # Final aggregation - using department_id as key, aggregated the total numOrdered and firsts
    results = []
    for k, v in aggDept.items():
        deptID = k
        numOrdered_lst = [row[0] for row in v]
        num_orders = sum(numOrdered_lst)
        firsts_lst = [row[1] for row in v]
        firsts = sum(firsts_lst)
        ratios = firsts / float(num_orders)
        resOut = deptID, num_orders, firsts, ratios
        results.append(resOut)

    # Build report.csv file
    outFile = open(fileC, 'w')
    outFile.write("department_id,number_of_orders,number_of_first_orders,percentage\n") # header row

    for line in sorted(results, key=lambda row: int(row[0]), reverse=False):
        department_id = line[0]
        number_of_orders = "{}".format(line[1])
        number_of_first_orders = "{}".format(line[2])
        percentage = "{0:.2f}".format(line[3])
        newline = "{},{},{},{}".format(department_id,number_of_orders,number_of_first_orders,percentage)
        outFile.write(newline+'\n')
    outFile.close()

if __name__ == "__main__":
    purchase_analytics(sys.argv[1], sys.argv[2], sys.argv[3])
