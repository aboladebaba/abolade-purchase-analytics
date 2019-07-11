import csv, sys

def purchase_analytics(fileA, fileB, fileC):

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
        rawProd = {}
        for line in raw:
            temp = rawProd.get(line[0], [])
            temp.append(line[3])
            rawProd[line[0]] = temp
    fhb.close()
    # Sanity check to ensure no single product is associated with multiple departments
    # This should give an empty list 
    #prodMultipleDept = [k for k,v in deptProd.items() if len(v) > 1] # this list was empty

    # Merge the two dict objects
    merged = { key: (rawOrders[key], rawProd[key]) for key in rawOrders}
    
    #Build a dict object with Department_id as key 
    aggDept = {}
    for key, val in merged.items():
        dept = val[1][0]
        numProds = len(val[0])
        numFirst = val[0].count('0')
        res = numProds, numFirst
        temp = aggDept.get(dept, [])
        temp.append(res)
        aggDept[dept] = temp

    # Final aggregation
    results = []
    for k, v in aggDept.items():
        deptID = k
        orderlst = [row[0] for row in v]
        num_orders = sum(orderlst)
        firstlst = [row[1] for row in v]
        firsts = sum(firstlst)
        ratios = firsts / num_orders
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